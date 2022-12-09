from array import *
file1 = open('input.txt', 'r')
# file1 = open('exData.txt', 'r')

forest = file1.readlines()
forest = [line.strip() for line in forest]

cols = len(forest[0])
rows = len(forest)
def walkNorth(tree, x, startY):
    dist = 0
    while startY != 0:
        startY -= 1         
        dist += 1    
        if forest[startY][x] >= tree: return dist
    return dist

def walkSouth(tree, x, startY):
    dist = 0
    while startY != rows - 1:
        startY += 1
        dist += 1
        if forest[startY][x] >= tree: return dist
    return dist

def walkEast(tree, startX, y):
    dist = 0
    while startX != 0:
        startX -= 1
        dist += 1
        if forest[y][startX] >= tree: return dist
    return dist

def walkWest(tree, startX, y):
    dist = 0
    while startX != cols - 1:
        startX += 1
        dist += 1
        if forest[y][startX] >= tree: return dist
    return dist

treesChecked = 0
outsideTrees = 0
highestScenicScore = 0
for y in range(rows):
    for x in range(cols):
        tree = forest[y][x]           
        treesChecked += 1
        visibleNorth = walkNorth(tree, x, y)
        visibleSouth = walkSouth(tree, x, y)
        visibleEast = walkEast(tree, x, y)
        visibleWest = walkWest(tree, x, y)
        # print(f"Tree {tree} {x},{y} N:{visibleNorth} S:{visibleSouth} E:{visibleEast} W:{visibleWest} ")
        scenicScore = visibleNorth * visibleSouth * visibleEast * visibleWest
        if scenicScore > highestScenicScore: 
            print(f"New High Score of {scenicScore}")
            highestScenicScore = scenicScore

print(f"Highest Scenic Score: {highestScenicScore}")
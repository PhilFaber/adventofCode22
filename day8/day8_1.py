from array import *
file1 = open('input.txt', 'r')
# file1 = open('exData.txt', 'r')

forest = file1.readlines()
forest = [line.strip() for line in forest]

cols = len(forest[0])
rows = len(forest)
def walkNorth(tree, x, startY):
    while startY != 0:
        startY -= 1             
        if forest[startY][x] >= tree: return False
    return True

def walkSouth(tree, x, startY):
    while startY != rows - 1:
        startY += 1
        if forest[startY][x] >= tree: return False
    return True

def walkEast(tree, startX, y):
    while startX != 0:
        startX -= 1
        if forest[y][startX] >= tree: return False
    return True

def walkWest(tree, startX, y):
    while startX != cols - 1:
        startX += 1
        if forest[y][startX] >= tree: return False
    return True

print(forest)
visibleTreeCount = 0
treesChecked = 0
outsideTrees = 0
for y in range(rows):
    for x in range(cols):
        tree = forest[y][x]           
        treesChecked += 1
        if x == 0 or y == 0 or x == cols - 1 or y == cols - 1:
            visibleTreeCount += 1
            outsideTrees += 1
        else:            
            visibleNorth = walkNorth(tree, x, y)
            visibleSouth = walkSouth(tree, x, y)
            visibleEast = walkEast(tree, x, y)
            visibleWest = walkWest(tree, x, y)
            # print(f"Tree {tree} {x},{y} N:{visibleNorth} S:{visibleSouth} E:{visibleEast} W:{visibleWest} ")
            if visibleNorth or visibleSouth or visibleEast or visibleWest:                                
                visibleTreeCount += 1


print(f"Trees Checked: {treesChecked} Outside Trees: {outsideTrees} Visible Trees: {visibleTreeCount}")
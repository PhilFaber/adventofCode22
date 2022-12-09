from array import *
# file1 = open('input.txt', 'r')
file1 = open('exData.txt', 'r')

rules = [line.strip() for line in file1.readlines()]

# === Biz Rules ===
# In col or row - follow same dir
# Not in same col - move dia
# Not in same row - mov dia

for rule in rules:
    split = rule.split(" ")
    direction = split[0]
    numberOfTimes = split[1]
    print(f"Moving {direction} - {numberOfTimes} times")
    for t in range(int(numberOfTimes)):
        if direction is "U":
            print("Moving Up")
        elif direction is "D":
            print("Moving Down")
        elif direction is "L":
            print("Moving Left")
        elif direction is "R":
            print("Moving Right")




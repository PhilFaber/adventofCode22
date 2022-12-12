from array import *
file1 = open('input.txt', 'r')
# file1 = open('prob2ExData.txt', 'r')
rules = [line.strip() for line in file1.readlines()]

class Point:
    def __init__(self, col=0, row=0):
        self.col = col
        self.row = row
    
    def __str__(self):
        return str(self.col) + "," + str(self.row) 

    def __eq__(self, other):
        # print(f"Testing Equality: {self} = {other}")
        return (self.col, self.row) == (other.col, other.row)


def isHAbove(hLoc, tLoc):    
    if hLoc.col == tLoc.col and hLoc.row > tLoc.row : return True
    return False

def isHBelow(hLoc, tLoc):
    if hLoc.col == tLoc.col and hLoc.row < tLoc.row : return True
    return False

def isHLeft(hLoc, tLoc):
    # print(f"isLeft: {hLoc.row}, {tLoc.row} : {hLoc.row == tLoc.row} and {hLoc.col < tLoc.col}")
    if hLoc.row == tLoc.row and hLoc.col < tLoc.col: return True
    return False

def isHRight(hLoc, tLoc) :
    if hLoc.row == tLoc.row and hLoc.col > tLoc.col: return True
    return False

def isDiagHTL(hLoc, tLoc) :
    if hLoc.col < tLoc.col and hLoc.row > tLoc.row: return True
    return False

def isDiagHTR(hLoc, tLoc) :
    if hLoc.col > tLoc.col and hLoc.row > tLoc.row: return True
    return False

def isDiagHBL(hLoc, tLoc) :
    if hLoc.col < tLoc.col and hLoc.row < tLoc.row: return True
    return False

def isDiagHBR(hLoc, tLoc) :
    if hLoc.col > tLoc.col and hLoc.row < tLoc.row: return True
    return False

def areTouching(hLoc, tLoc):   
    colNotTouch = abs(tLoc.col - hLoc.col) >= 2
    rowNotTouch = abs(tLoc.row - hLoc.row) >= 2
    
    # print(f"col: {colNotTouch} and row: {rowNotTouch}")
    if (colNotTouch or rowNotTouch):
        print("Not Touching")
        return False
    else:
        print("Touching")
        return True



def moving(hLoc, tLoc):
    print(f"\nMoving: h{hLoc}, t{tLoc}")        
    if areTouching(hLoc, tLoc):   
        print("Touching...")         
        return Point(tLoc.col, tLoc.row)
    elif isHAbove(hLoc, tLoc):
        print("Moving U")  
        return Point(tLoc.col, tLoc.row + 1)
    elif isHBelow(hLoc, tLoc):
        print("Moving D")
        return Point(tLoc.col, tLoc.row - 1)
    elif isHLeft(hLoc, tLoc):
        print("Moving L")  
        return Point(tLoc.col - 1, tLoc.row)
    elif isHRight(hLoc, tLoc):  
        print("Moving R")      
        return Point(tLoc.col + 1, tLoc.row)
    elif isDiagHTR(hLoc, tLoc):
        print("Moving Dia TR")      
        return Point(tLoc.col + 1, tLoc.row + 1)
    elif isDiagHTL(hLoc, tLoc):
        print("Moving Dia TL")      
        return Point(tLoc.col - 1, tLoc.row + 1)
    elif isDiagHBR(hLoc, tLoc):
        print("Moving Dia BR")      
        return Point(tLoc.col + 1, tLoc.row - 1)
    elif isDiagHBL(hLoc, tLoc):
        print("Moving Dia BL")      
        return Point(tLoc.col - 1, tLoc.row - 1)

print("\n\n=========RUNNING=========\n\n")
locationsBeen=[Point(0,0)]

knots = [Point(0,0) for i in range(10)]

# for rule in rules[0:1]:
for rule in rules:
    split = rule.split(" ")
    direction = split[0]
    numberOfTimes = split[1]
    print(f"=== Moving {direction} - {numberOfTimes} times ===")
    for t in range(int(numberOfTimes)):
        print(f"***** Moving {direction} - {numberOfTimes} times *****")    
        hLoc = knots[0]
        # Move Head     
        if direction == "U":
            hLoc.row += 1            
        elif direction == "D":
            hLoc.row -= 1              
        elif direction == "L":
            hLoc.col -= 1            
        elif direction == "R":
            hLoc.col += 1
            
       
        # Followers Follow!  
        
        for i in range(len(knots) - 1):            
            frontKnot = knots[i]
            follow = i + 1
            followKnot = knots[follow]
            print(f"Moving knot {i}")
            knots[follow] = moving(frontKnot, followKnot)
            
        
        # Check it!   
        tailKnot = knots[9]
        print(f"New Tail Location: {tailKnot}")
        if tailKnot not in locationsBeen:
                locationsBeen.append(tailKnot)

    # print("\n")
# for loc in locationsBeen:
#     print(loc)
    
print(f"Output: {len(locationsBeen)}")




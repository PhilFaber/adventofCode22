
from anytree import Node, RenderTree
import re
# file1 = open('dayInput.txt', 'r')
file1 = open('exData.txt', 'r')
data = file1.readlines()
data = [line.strip() for line in data]

# Find sizes of each directory
# Find directories with total size <= 10000

# Ideas
# Find sizes of all dirs
# Then find dirs within dirs and total size

def findNextCommand(lines):
    for x in range(len(lines)):        
        line = lines[x]
        if line.startswith('$'):
            return x + 1
    return len(lines) + 1

def getItemSize(item):
    match = re.search(r'\d+', item)
    if match:
        return int(match.group()) 


def getDirSize(dirName, dirDict):
    print (f"************** {dirName}")    
    dirList = dirDict[dirName]
    if any("dir" in item for item in dirList):
        matching = [s for s in dirList if "dir" in s]        
        dirSize = 0
        for dir in matching:
            # print("Going recursive!!!!")
            dirSize += getDirSize(dir.split()[-1], dirDict)
        for x in dirList:
            if "dir" not in x:
                dirSize += getItemSize(x)
        return dirSize
    else:
        # print (f"Terminating on dirName {dirName}")
        dirSize = 0
        for item in dirList:
            # print(item)
            match = re.search(r'\d+', item)
            if match:
                dirSize += int(match.group())
        # print(f"dir {dirName} is size {dirSize}")
        return dirSize            
               
    

cwd = ""
#Flatten it!
dirDict = {}
print("")
for x in range(len(data)):
    line = data[x]  
    if line.startswith("$ ls"):
        dirName = data[x-1][4:].replace(" ", "")        
        numberOfItemsInDir = findNextCommand(data[x+1:])
        # print(f"Number of items in {dirName} dir: {numberOfItemsInDir}")
       
        itemsInDir = data[x + 1 : x + numberOfItemsInDir]
        # print(f"items in {dirName} dir: {itemsInDir}")        
        dirDict.update({cwd : itemsInDir})        
        print("")
    elif line.startswith("$ cd"):
        cdCmd = line.split(" ")[-1]
        if cdCmd == "..":
            cwd = cwd[0:cwd.rfind("/")]
        elif cdCmd == "/":
            cwd = "/"
        else: 
            if cwd is "/":
                cwd += cdCmd
            else:
                cwd += "/" + cdCmd
        print(cwd)


print("~~~~~~~ File Struct ~~~~~~~")
for dirName in dirDict:
    print(f"{dirName} : {dirDict[dirName]}")

#Calculate it!
# print ("====== Calculating sizes =======")
# dirSizeDict = {}

# for dirName in dirDict:
#     dirSizeDict.update({dirName : getDirSize(dirName, dirDict)})

# sumOfDirSizes = 0
# for dirName in dirSizeDict:
#     dirSize = dirSizeDict[dirName]
#     if dirSize <= 100000 :
#         print(f"Adding dir {dirName} : {dirSize}")
#         sumOfDirSizes += dirSize
# print(f"Output: {sumOfDirSizes}")

        
  






                
            
            

    

        








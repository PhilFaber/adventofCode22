import re
file1 = open('day5DataStart.txt', 'r')
# file1 = open('exData.txt', 'r')
starting = file1.readlines()  

# Transform Data
yStacks = []
stackCount = len(re.findall('....',starting[0])) + 1
print(stackCount)
for line in starting:
# for line in starting[:2]:
    yLines = []
    blocks = re.findall('....',line)
    if not re.search('[0-9]', line):      
        for block in blocks:
            if re.search('[a-zA-Z]', block):            
                block = block.replace('[', '')
                block = block.replace(']', '')
                block = block.replace(' ', '')
                yLines.append(block)
            else:
                yLines.append(' ')
        yStacks.append(yLines)

print(yStacks)
print ('\n')



# Initialize x data struct
xStacks = []
for i in range(stackCount - 1):
    xStacks.append([]) 

# # Convert to X data struct
for stack in yStacks:
    # stack.reverse()
    for i in range(len(stack)):
        xStacks[i].append(stack[i])

for stack in xStacks:
    while ' ' in stack:
        stack.remove(' ') 
    stack.reverse()

print(xStacks)

#Let's do this
file2 = open('day5DataRules.txt', 'r')

rules = file2.readlines()
for rule in [line.strip() for line in rules]:
# for rule in [line.strip() for line in rules[:3]]:
    print(rule)
    num = re.findall(r'\d+', rule)
    numToMove = int(num[0])
    fromStack = int(num[1]) - 1
    toStack = int(num[2]) - 1

    crane = []

    print("from stack: " + str(xStacks[fromStack])) 
    for i in range(numToMove):
        box = xStacks[fromStack].pop()        
        crane.append(box)
    crane.reverse()
    print("Crane: " + str(crane))
            
    for box in crane:
        xStacks[toStack].append(box)
    for stack in xStacks:
        print(stack)
        

output = ""
for top in xStacks:
    output += top.pop()
print (output)



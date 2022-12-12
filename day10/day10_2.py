from array import *
file1 = open('input.txt', 'r')
# file1 = open('exData.txt', 'r')
rules = [line.strip() for line in file1.readlines()]

drawingPos = 0
spritePos = 1
opCountdown = 0
cycle = 1

fRules = []
print("\n\n\n======== Running ========")
# for r in rules[0:12]:
for r in rules:
    fRules.append(r.split())

fRules.reverse()
rule = fRules.pop()
if rule[0] == "addx":     
    opCountdown = 2
else:
    opCountdown = 1

str = ""
crt = []

while len(fRules) != 0:    
    if opCountdown == 0:
        if rule[0] == "addx": 
            print(f"Adding {rule[1]} to {spritePos}")
            value = int(rule[1])
            spritePos += value
            opCountdown = 2
        else:            
            opCountdown = 1          
        rule = fRules.pop()   
    
    
    if spritePos == drawingPos or spritePos + 1 == drawingPos or spritePos - 1 == drawingPos: 
        str += "#"
    else: 
        str += "."

    if len(str) == 40:
        print("\nNewline!\n")
        crt.append(str)
        str = ""
        drawingPos = 0
    else:
        drawingPos += 1

    opCountdown -= 1    
    cycle += 1
    print(f"cycle: {cycle}, opCountdown {opCountdown}, drawingPos: {drawingPos}, spritePos: {spritePos}")

for line in crt: print(line)
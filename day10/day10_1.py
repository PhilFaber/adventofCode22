from array import *
file1 = open('input.txt', 'r')
# file1 = open('exData.txt', 'r')
rules = [line.strip() for line in file1.readlines()]

MONITOR_RATE = 40
output = 0
clock = 0
register = 1

fRules = []
print("\n\n\n======== Running ========")
# for r in rules[0:12]:
for r in rules:
    fRules.append(r.split())

fRules.reverse()
rule = fRules.pop()

while clock < 10000000 and len(fRules) != 0:
    # print(rule)
    if rule[0] == "noop": 
        clock += 1        
        rule = fRules.pop()
        if clock == 20 or (clock-20)%MONITOR_RATE == 0:
            output += register*clock
            print(f"--Register is {register} at {clock}. Updating output to output to {output}")
    else:
        value = int(rule[1])
        for i in range(2):            
            clock +=1
            if clock == 20 or (clock-20)%MONITOR_RATE == 0:
                output += register*clock
                print(f"Register is {register} at {clock}. Updating output to output to {output}")

        register += value    
        print(f"Adding {value} to Register: New: {register} at {clock}")        
        rule = fRules.pop() 

print(f"Output: {output}")
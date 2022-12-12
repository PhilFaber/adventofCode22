import re
import math

class Monkey:
    def __init__(self, name = "", items=[], operationString = "", test = 0, trueThrow = 0, falseThrow = 0, timesInspected = 0):
        self.name = name
        self.items = items
        self.operationString = operationString
        self.test = test
        self.trueThrow = trueThrow
        self.falseThrow = falseThrow
        self.timesInspected = timesInspected
    
    def __str__(self):
        return "Monkey " + self.name + ":" + str(self.items)
        # return "Monkey " + self.name + ":" + str(self.items) + " ops: " + self.operationString + " test: " + str(self.test) +   " true: " + str(self.trueThrow) + " false: " + str(self.falseThrow)

    # def __eq__(self, other):
    #     # print(f"Testing Equality: {self} = {other}")
    #     return (self.col, self.row) == (other.col, other.row)

def operateOnItem(item, operationString):    
    splits = operationString.split(' ')    
    val1 = 0    
    if splits[0] == "old": 
        val1 = item
    else:
        val1 = int(splits[0])   

    val2 = 0
    if splits[2] == "old": 
        val2 = item
    else:
        val2 = int(splits[2])

    if splits[1] == "*":
        return val1 * val2

    if splits[1] == "+":
        return val1 + val2



file = open('input.txt', 'r')
# file = open('exData.txt', 'r')
data =  file.read()

print("\n\n\n======== Running ========")
monkeys = []

# Parse Data
rawStartingItems = re.findall('Starting items:.*', data)
rawOps = re.findall('Operation:.*', data)
rawDivisibleBy = re.findall('Test:.*', data)
rawTrueThrow = re.findall('true:.*', data)
rawFalseThrow = re.findall('false:.*', data)

for i in range(len(rawStartingItems)):
    monkeys.append(Monkey(str(i)))
    monkeysItems = re.findall("\d+", rawStartingItems[i])
    intItems = []
    for items in  monkeysItems: intItems.append(int(items))
    monkeys[i].items = intItems
    monkeys[i].operationString = str(rawOps[i][17:])    
    monkeys[i].test = int(re.findall("\d+", rawDivisibleBy[i])[0])
    monkeys[i].trueThrow = int(re.findall("\d+", rawTrueThrow[i])[0])
    monkeys[i].falseThrow =int(re.findall("\d+", rawFalseThrow[i])[0])
     

for monkey in monkeys:
    print(monkey)



#Run the rounds
for i in range(20):
# for monkey in monkeys[:2]:
    for monkey in monkeys:       
            # Monkey Inspects item
            print(monkey.items)
            for item in monkey.items:
                monkey.timesInspected += 1
                # Increase Worry
                worry = operateOnItem(item, monkey.operationString)
                print(worry)
                # Divide by Three and round
                worry = math.trunc(int(worry)/3)
                # Monkey Test then throw
                if worry % monkey.test == 0:
                    print(f"Throwing {item} now of {worry} to {monkey.trueThrow}")
                    monkeys[monkey.trueThrow].items.append(worry)
                else:
                    print(f"Throwing {item} now of {worry} to {monkey.falseThrow}")
                    monkeys[monkey.falseThrow].items.append(worry)
            monkey.items = []

print("\n====Output time!====")
for monkey in monkeys:
    print(monkey)

for monkey in monkeys:
    print(monkey.timesInspected)
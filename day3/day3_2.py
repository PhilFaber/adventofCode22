file1 = open('day3_data.txt', 'r')
lines = file1.readlines()  

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

def getValue(varFound): 
    if varFound.islower():
        value = ord(varFound) - 96
        print(ord(varFound))
    else:   
        value = ord(varFound) - 38
        print(ord(varFound))
    return value


output = 0
formattedLines = [line.strip() for line in lines]
groups = [formattedLines[i:i+3] for i in range(0, len(formattedLines), 3)] 
varFound = ""
for group in groups:
    for sack in group:
        print ("Looking at sack: " + sack + " and group: " + group[0] + "," + group[1] + "," + group[2])
        for char in sack:            
            if char in group[0] and char in group[1]:
                varFound = char
    output += getValue(varFound)

print(output)
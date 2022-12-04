file1 = open('day3_data.txt', 'r')
lines = file1.readlines()  

#each line is a sack, wiht 2 compartments
#each sack has equal number of items in each compartments

# Lowercase item types a through z have priorities 1 through 26.
# Uppercase item types A through Z have priorities 27 through 52.

### CODE
# 1) Split into half
# 2) look for dupes
# 3) Check char's value
# 4) add them values up
output = 0
for x in lines:

    first_half  = x[:len(x)//2]
    second_half = x[len(x)//2:]

    varFound = ""
    value = 0
    for char in first_half:
        if char in second_half:
            print("First: " + first_half + " Second: " + second_half)
            varFound = char
            if varFound.islower():
                value = ord(varFound) - 96
                print(ord(varFound))
            else:   
                value = ord(varFound) - 38
    print("Found: " + varFound + " Value: " + str(value))
    output += value

print("Final: " + str(output))



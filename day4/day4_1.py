file1 = open('day4_data.txt', 'r')
lines = file1.readlines()  

output = 0
for pairs in [line.strip() for line in lines]:
# for pairs in [line.strip() for line in lines[:2]]:
    pairsSplt = pairs.split(",")
    elf1 = pairsSplt[0].split("-")
    elf2 = pairsSplt[1].split("-")

    elf1[0] = int(elf1[0])
    elf1[1] = int(elf1[1])
    elf2[0] = int(elf2[0])
    elf2[1] = int(elf2[1])
    
    if (elf1[0] >= elf2[0] and elf1[1] <= elf2[1]) or (elf2[0] >= elf1[0] and elf2[1] <= elf1[1]):
        print("Subset found" + str(elf1) + "," + str(elf2))
        output += 1

print(output)
file1 = open('day4_data.txt', 'r')
# file1 = open('exData.txt', 'r')
lines = file1.readlines()  

output = 0
for pairs in [line.strip() for line in lines]:
    pairsSplit = pairs.split(",")
    elf1 = pairsSplit[0].split("-")
    elf2 = pairsSplit[1].split("-")

    elf1[0] = int(elf1[0])
    elf1[1] = int(elf1[1])
    elf2[0] = int(elf2[0])
    elf2[1] = int(elf2[1])

    if (elf1[0] == elf1[1]):
        elf1Range = [elf1[0]]
    else:
        elf1Range = list(range(elf1[0], elf1[1]))

    if (elf2[0] == elf2[1]):
        elf2Range = [elf2[0]]
    else:
        elf2Range = list(range(elf2[0], elf2[1]))

    print("Elf1: " + str(elf1Range) + " Elf2: " + str(elf2Range))
    if (elf1[0] in elf2Range or elf1[1] in elf2Range) or (elf2[0] in elf1Range or elf2[1] in elf1Range):
        print("Found overlap!")
        output +=1

print(output)
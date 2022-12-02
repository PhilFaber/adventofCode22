from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Starting day1.py at ", current_time)

# Using readlines()
file1 = open('day1_data.txt', 'r')
Lines = file1.readlines()  

maxCal = 0
runCal = 0
for line in Lines:    
    if line.strip():
        runCal += int(line)
    else:
        print("Found New Elf. Prev Running Cal " + str(runCal) + " maxCal: " + str(maxCal))              
        if runCal > maxCal:
                print("Found New Max Cal!!! Old: " + str(maxCal) + "New: " + str(runCal))
                maxCal = runCal
        runCal = 0

print("Final Max: " + str(maxCal))

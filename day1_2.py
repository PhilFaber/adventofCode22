from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Starting day1.py at ", current_time)

# Using readlines()
file1 = open('day1_data.txt', 'r')
Lines = file1.readlines()  

runCal = 0
topCalsList = [0, 0, 0]
print (topCalsList)
for line in Lines:    
    if line.strip():
        runCal += int(line)
    else:         
        for i in range(len(topCalsList)):
            maxCalItr = topCalsList[i]
            if runCal > maxCalItr:  
                print("Found New Max Cal!!! Old: " + str(maxCalItr) + " New: " + str(runCal))
                topCalsList[i] = runCal
                topCalsList.sort()
                break;                
        runCal = 0
print (topCalsList)
print ("Total Cals: " + str(sum(topCalsList)))



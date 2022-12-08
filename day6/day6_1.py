from queue import Queue
file1 = open('dayInput.txt', 'r')
data = file1.readline()  
# data = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

# Find first instance where 4 characters have a duplicate

output = 0
unread = []
[unread.append(char) for char in data]
buffer = []
for i in range(14):
    buffer.append(unread.pop(0))

print(buffer)

for i in range(len(data)):
    listLen = len(buffer)
    setLen = len(set(buffer))
    print(f"buffer: {buffer} listLen: {listLen} setLen: {setLen}")
    if listLen == setLen:    
        output = i + 14
        break;
    else:
        buffer.pop(0)
        buffer.append(unread.pop(0))

print(output)







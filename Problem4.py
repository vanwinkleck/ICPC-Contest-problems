num = input()
y=[]
total=0
z=[]
repeat=0

for i in range(0,len(num),1):
    y.append(num[i:i+1])
    for i in range(0, len(y),1):
        total += int(y.pop())

for i in range(0,len(str(total)),1):

    z.append(str(total)[i:i+1])
    for i in range(0, len(z),1):
        repeat += int(z.pop())
print(repeat)

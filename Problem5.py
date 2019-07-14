str=input('')
list =[]
max = 0
sent = []
while (str!= "Done"):
    sent.append(str)
    list.append(len(str))
    if (max<len(str)):
        max = len(str)
    str=input('')
for i in range(max):
    for j in range(len(list)):
        if(list[j]>i):
            print(sent[j][i], end= '')
        else:
            print(' ', end = '')
    print()

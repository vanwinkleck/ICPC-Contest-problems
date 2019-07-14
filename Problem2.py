t = 0
t1 = 0
t2 = 0
speed = 0
miles = 0

count = 0
times = []
end = ''
userInput = ''
while end != 'Done':
    userInput = input()
    count +=1
    try:
        speed,t = userInput.split(' ')
        times.append(t)
        if count == 1:
            miles += (int(speed)*int(t))
        else:
            t1 = times[(count-1)]
            t2 = times[(count-2)]
            miles += (int(speed)*(int(t1)-int(t2)))
    except ValueError:
        end = userInput
        

print(miles,'miles')

    

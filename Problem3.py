numbers = input('Enter a sequence of numbers: ')
numList = numbers.split(' ')

def large(numList):
    largest = numList[0]
    largest2 = None

    for x in numList[1::]:
        if x > largest:
            largest2 = largest
            largest = x
        elif largest2 == None or largest2 < x:
            largest2 = x

    print('the two largest numbers are: ' + largest2, largest)
large(numList)
    

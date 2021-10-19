import random

randomlist = []

number = int(input("Enter the number of numbers you want to have in your array:"))

for i in range(0,number):
    n = random.randint(1,150)
    if n in randomlist:
        print('pass')

    else:
        
        randomlist.append(n)
    print(randomlist)
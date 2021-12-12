import math
import random
a = []   #initialize list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
a.append(random.randint(1, 99))   #  add element to list
for i in range(10):   # loop through elements of the list
    g = int(input("Enter an integer from 1 to 99: "))  #  type a number 
    while a[i] != g:  # the loop continues until a[i] == 0
        if g < a[i]:   # when g is lower than a[i]
            print("guess is low")   # print a message
            g = int(input("Enter an integer from 1 to 99: "))
        elif g > a[i]:   # when g is greater than a[i]
            print("guess is high")   # print a message
            g = int(input("Enter an integer from 1 to 99: "))
        else:
            break    # end loop
    print("you guessed it!")

b = []
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
b.append(random.randint(1, 49))
for i in range(10):
    g = int(input("Enter an integer from 1 to 49: "))
    while b[i] != g:
        if g < b[i]:
            print("guess is low")
            g = int(input("Enter an integer from 1 to 49: "))
        elif g > b[i]:
            print("guess is high")
            g = int(input("Enter an integer from 1 to 49: "))
        else:
            break
    print("you guessed it!")
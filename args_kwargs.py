import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

#Args and KWArgs are inputs with out a set limit of them.
#  *args, and **kwargs

def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0],kwargs['food']))

myfunc(10,20,30,fruit='orange', food='eggs',animal='dog')

# -----------

def myfunc1(*args):
    return sum(args)

def myfunc2(*args):
    myList = []
    for item in args:
        if item%2==0:
            myList.append(item)
    return myList

print(myfunc2(-1,-2,4,3,5))


# lower to upper, odd even
def myfunc3(s):
    charList = list(s)
    newstring = ""
    x = 0
    while x < len(charList):
        if x%2==0:
            newstring = newstring + charList[x].lower()
        else:
            newstring = newstring + charList[x].upper()
        x += 1

    return newstring


print(myfunc3('this is a much longer strings12 3'))
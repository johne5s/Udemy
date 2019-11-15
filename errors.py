import os
import sys
import time
import math
from random import randint

clear = lambda: os.system('cls') #on Windows System
clear()

funnyList = ["Whoops! That's not a number", "Try again, You can't fool me","What do you thik this is?"]

def getFunny():
    return randint(0,len(funnyList)-1)


while True:
    try:
        #code to be attempted
        result = int(input("Please provide a number: "))
    except TypeError:
        print("A TypeError was found")
        continue
    except OSError:
        print("an OSError was found")
        continue
    except FloatingPointError:
        print("A FloatingPointError was found")
        continue  
    except:
        print(funnyList[getFunny()])
        continue
    else:
        # No error so do the else
        print("Yes, that is a nice looking number")
        break

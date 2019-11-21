import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

def welcome_function():
    print("Welcome from func1")

def welcome_function2():
    print("func 2 printed")

def make_full_name(first, last):
    name = f"{last}, {first}"
    return name

welcome_function()
welcome_function2()

fullname = make_full_name("John", "Smith")
print(fullname)

def get_bid():
    while True:
        try:
            user_entry = int(input("How much to bet?"))
        except:
            print("Not an int")
            continue
        else:
            return user_entry

get_bid()

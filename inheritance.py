import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

class Animal():
    def __init__(self):
        print("Animal Created")

    def who_ami(self):
        print("i am an animal")
    
    def eat(self):
        print("I am eating")

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("a dog was created")
    
    def who_ami(self):
        print("I'm a dog")

    def bark(self):
        print("WOOF Woof")

mydog = Dog()
mydog.who_ami()
mydog.bark()
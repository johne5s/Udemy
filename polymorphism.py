import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

class Animal():
    def __init__(self,name):
        self.name = name
        print("Animal was created")

    def speak(self):
        raise NotImplementedError("Subclass - You should override this")

    def who_am_i(self):
        print("i am an animal with the name " + self.name)
    
    def eat(self):
        print("I am eating")

class Dog(Animal):
    def speak(self):
        return self.name + " says woof"

class Cat(Animal):
    def speak(self):
        return self.name + " says Meow"

niko = Dog("Niko")
maya = Cat("Maya")

#maya.who_am_i()
#niko.who_am_i()

#print(niko.speak())
#print(maya.speak())

#now for the poly stuff.  Both dog and cat share the same skeak function.
#for pet in [niko,maya]:
#    print(type(pet))
#    print(pet.speak())

#now we create a function that calls the speak even though they are in differnt classes
def pet_speak(pet):
    print(pet.speak())

pet_speak(niko)
pet_speak(maya)
niko.speak()

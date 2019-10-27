import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

myList = [1,2,3,4,5]

#built in help function
help(myList.insert)
clear()

#functions
def my_func():
    '''
    Doc strings are good to have
    the built in help function will reed the doc string 
    '''
    print("Hello Func")

#call the function
my_func()


#pass in values
def say_hello1(name='NAME'):
    print('your name is ' + name)

say_hello1('john')

#return a value from a function
def say_hello2(name='NAME'):
    return 'your name is ' + name

say_hello2('john')

#add two numbers and return the answer
def addTwo(n1,n2):
    return n1+n2

print(addTwo(4,7))


#two examples
def dog_check(dogstring):
    if 'dog' in dogstring.lower():
        return True
    else:
        return False

print(dog_check('my dog ran away')) #true
print(dog_check('my cat ran away')) #false
print(dog_check('my Dog ran away')) #true

def dog_check2(dogstring):
    return 'dog' in dogstring.lower()

print(dog_check2('my dog ran away')) #true
print(dog_check2('my cat ran away')) #false
print(dog_check2('my Dog ran away')) #true

#pig Latin!
def pig_latin(word):
    first_letter = word[0]

    #check if first letter is a vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] +first_letter + 'ay'
    return pig_word

print(pig_latin("apple"))
print(pig_latin("Apple"))
print(pig_latin("wood"))
print(pig_latin("Chicken"))

def check_bool(a):
    if a:
        return 'Hello'
    else:
        return 'Goodbye'

print(check_bool(False))
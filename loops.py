import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

# loops
my_object = [1,2,3,4,5,6]
print("print Even")
for item_name in my_object:
    if item_name % 2 == 0:
        print(f'{item_name}')

print("print odd")
for item_name in my_object: 
    if item_name % 2 > 0:
        print(f'{item_name}')

string_loop = 'My String Loop'
for letter in string_loop:
    print(letter)

for letter in 'string_loop with out var':
    print(letter)


#while loops
x = 0
while x < 5:
    print(f'The value is {x}')
    x += 1
else:
    print(f'x is Not less then 5: {x}')

# break, exit the loop
# continue, same as return, goes to the top of the loop to get the next item 
# pass, do nothing
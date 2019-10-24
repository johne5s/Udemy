import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()


#Lists
num_list = [3,7,2,3,56,21]
print(num_list)

#Dictionary
my_dict = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
print(my_dict['key2'])
my_dict['K1'] = 'inserted'
print(my_dict)
print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

#Tuple
my_Tup = (1,2,3,'a','a','a','a')
my_list = [1,2,3]
print(my_Tup.count('a'))
print(my_Tup.index('a'))

#sets
my_set = set('Mississippi')
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(5)
my_set.add(1)

my_set2 = set([1,1,2,3])
print(my_set2)

#bool - True and False

clear()
#input output files
#open a file option 1
myfile = open('myfile.txt')
myfile.write
print(myfile.read())
print(myfile.read())
myfile.seek(0) #move the curser back to the start of the file
print(myfile.readlines()) # creates a list.
myfile.close()

#open a file option 2
#read a file
with open('myfile.txt',mode='r') as my_new_file:
    contents = my_new_file.readlines()
    print(contents)

#append
with open('myfile.txt',mode='a') as my_new_file:
    contents = my_new_file.write('\nline was appended')
    print(contents)

#write
with open('blabla.txt',mode='w') as f:
    f.write('saved a new file')
with open('blabla.txt',mode='r') as f:
    print(f.read())

clear()

x = 150 - 100 + (10 * 5) + 0.25
x = 4 * (6 + 5)
x = 4 * 6 + 5
x = 4 + 6 * 5
print(x)

i = 3 + 1.5 + 4
print(type(i))

print(math.sqrt(4))

clear()


#review question

s = "Hello"
print(s[-1])
print(s[4])
print(s[::-1]) #revise order

num_lista = [0,0,0]
print(num_lista)
num_listb = []
num_listb.append(0)
num_listb.append(0)
num_listb.append(0)
print(num_listb)
num_listc = [0]*3 #use multiply to create a list
print(num_listc)

list3 = [1,2,3,'Hello']
print(list3)
list3[3] = 'GoodBye'
print(list3)

list4 = [5,3,4,6,1]
list4.sort()
print(list4)

d = {'simple_key':'hello1'}
print(d['simple_key'])
d = {'k1':{'k2':'hello2'}}
print(d['k1']['k2'])
d = {'k1':[1,2,{'k2':['tricky',{'tough':[1,2,['hello3']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])

list5 = [1,2,2,33,4,4,11,22,3,3,2]
list5a = set(list5)
print(list5a)

clear()
#Operators, AND, OR, NOT
a = 6
b = 3

if a==b:
    print("what")
elif a>b:
    print('where')
else:
    print('else')

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


clear()
mylist66 = [(1,2,3),(3,4,3),(5,6,3),(7,8,3)]
for nest in mylist66:
    for item in nest:
        print(item)
# or it can be done this way, called tuple unpacking
print('- OR -')
for (a,b,c) in mylist66:
    print(a)
    print(b)
    print(c)

#dictionary
d = {'k1':1,'k2':2,'k3':3,'k4':4,'k5':5,}
for item in d.items():
    print (item)

#or tupple unpacking
for key,value in d.items():
    print (key)


clear()
#while loops
x = 0
while x < 5:
    print(f'The value is {x}')
    x += 1
else:
    print('No less then 5')

# break, exit the loop
# continue, same as return, goes to the top of the loop to get the next item 
# pass, do nothing

#range generator
myRange = list(range(5,21,5))
for num in myRange:
    print(num)

#enumerat
index_count = 0
wordString = 'words are cool'
for letter in wordString:
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count += 1

print('------')
#this is how i normaly do a foor loop
index_count = 0
for letter in wordString:
    print(wordString[index_count])
    index_count += 1

print('------')
#this is how to do a enumerate, creates a tuple
for item in enumerate(wordString):
    print(item)

clear()
#zip fuction, joining 2 lists
ziplist1 = [1,2,3]
ziplist2 = ['a','b','c']
ziplist = zip(ziplist1,ziplist2)
for zipitem in ziplist:
    print(zipitem)

#check if something is in a list
print('p' in ziplist1)

# min max key words
print(min(ziplist1))
print(max(ziplist1))


#import on the fly
#random order of a list
from random import shuffle
myshuffle = [1,2,3,4,5,6,7]
shuffle(myshuffle)
print(myshuffle)

#get a random int
from random import randint
print(randint(0,30))

#user input
result = input('enter a number\n')
try:
    result = int(result)
    print (result)
except ValueError:
    print ('Please enter an integer')

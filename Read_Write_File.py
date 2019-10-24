import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
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
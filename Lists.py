import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

#Lists
num_listc = [0]*3 #use multiply to create a list
print(num_listc)
#or build by hand
num_list = [3,7,2,3,56,21]
print(num_list)

int_List = [1,2,3,4,5]
float_List = [1.1,2.2,3.3,4.4,5.5]
str_List = ["a","b","c","d","Hello"]

print(int_List)
print(float_List)
print(str_List)

#Dictionary
my_dict = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
print(my_dict['key2'])
my_dict['K1'] = 'inserted'
print(my_dict) #returns the dict object
print(my_dict.items())  #returns each key value pair
print(my_dict.keys()) #returns only the keys
print(my_dict.values()) #returns only the values
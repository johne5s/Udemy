import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

my_num = 10
print(my_num)
my_num2 = 1.5
my_num3 = 1/3
print(my_num3)

a = 27
b = a

print(a)
print(b)

b = 22

print(a)
print(b)

foo = "test"
bar = foo + "ing"
cat = bar * 2

print(cat)

print("my_num type is : ", type(my_num))
print("my_num2 type is : ", type(my_num2))
print("my_num3 type is : ", type(my_num3))
print("cat type is : ", type(cat))

print("\n")
# List and tupil

#list
l = ["x","y","z"]

#tupil
t = ("x","y","z")

print(l[0])
print(t[1])

l[1] = "M"
l.append("n")
print(l)

print("Test", end=" - ")
print("Test", end=" - ")
print("Test", end=" - ")
print("Test", end=" - ")
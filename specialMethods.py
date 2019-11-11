import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()

class Book():

    def __init__(self,title,author,pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} with {self.pages} number of pages"

    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book Object has been deleted")

b = Book("Python rocks", "John S", 200)
print(b)

del b
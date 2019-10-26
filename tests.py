import os
import sys
import time
import math

clear = lambda: os.system('cls') #on Windows System
clear()


st = 'Sam Print only the words that start with s in this sentence'
wordList = st.split(" ")
print(wordList)
#method 1
s_words = [word for word in wordList if word[0].lower() =="s"]
print(s_words)

#method2
for word in wordList:
    if word[0] =="s":
        print(word)

#print 0,10
numRange = [num for num in range(0,11) if num%2==0]
print(numRange)


#is divisible by 3?
mylist3 = [num for num in range(1,51) if num%3==0]
print(mylist3)


#check if the word is even in length
st = 'Print every word in this sentence that has an even number of letters'
wordList = st.split(" ")
for word in wordList:
    if len(word)%2==0:
        print(word + ' is even')


numList = [num for num in range(1,101)]
for num in numList:
    if num%3==0 and num%5==0:
        print(f"FuzzBizz {num}")
    elif num%3==0:
        print(f"Fizz {num}")
    elif num%5==0:
        print(f"Buzz {num}")
    else:
        print(num)


#create a list of the first letters
st = 'Create a list of the first letters of every word in this string'
stSplit = st.split(" ")
stringList = [word[0] for word in stSplit]
print(stringList)
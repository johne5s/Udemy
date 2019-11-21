''' Number Guessing Game '''

import random

from random import randint

def get_guess_number():
    while True:
        try:
            user_entry = int(input("What is your guess?"))
        except:
            print("Not an int")
            continue
        else:
            return user_entry

magic_number = randint(1,10)
print(magic_number)

print("I'm thinking of a number can you guess it")
correct_guess = False
guess_counter = 0

while not correct_guess:
    guess_number = get_guess_number()
    if guess_number == magic_number:
        print("You win")
        correct_guess = True
    elif guess_number < magic_number:
        print("Too low")
    else:
        print("Too high")
    guess_counter += 1

print(f"You are correct, my number was {magic_number}, you took {guess_counter} trys")


#run the main function

def main:
    print("I'm the main guy")

if __name__ == "__main__":
    main()




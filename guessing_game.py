#first off we need the random import
#then create a variable to represent the random computer
#the input of the human/text value

import random
thenumber = random.randint(1,20)
attempts = 0

while attempts <= 3:
    guess = int(input("enter your guess: "))
    attempts += 1

#if they get the guess correct then what?
    if guess > thenumber:
        print("Too high! try again: ")
    elif guess < thenumber:
        print("Too low! try again: ")
    else:
        print("You got it! Congratulations!")

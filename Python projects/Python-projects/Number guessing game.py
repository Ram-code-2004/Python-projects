
import random

num_to_guess = random.randint(1, 100)
while True:
    try:
        Guess = int(input("Guess the number between 1 to 100: "))

        if Guess < num_to_guess:
            print("Too low!")
        elif Guess > num_to_guess:
            print("Too high!")
        else:
            print("Congratulations! Your guess is correct")
            break
    except ValueError:
        print("please enter a valid number")

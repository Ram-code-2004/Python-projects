import random

choice = ["rock", "paper", "scissors"]

while True:
    user_input = input ("Enter rock, paper, or scissors (or 'q' to quit): ").lower()
    if user_input == "q":
        print("Thanks for playing!")
        break
    if user_input not in choice:
        print("Invalid input. Please try again.")
        continue
    computer_input = random.choice(choice)
    print(f"Computer chose: {computer_input}")

    if user_input == computer_input:
     print("It's a tie!")
    elif user_input == "rock" and computer_input == "scissors":
     print("You win! Rock beats scissors.")
    elif user_input == "paper" and computer_input == "rock":
     print("You win! Paper beats rock.")
    elif user_input == "scissors" and computer_input == "paper":
     print("You win! Scissors beats paper.")
    else:
     print("You lose! Try again.")
    
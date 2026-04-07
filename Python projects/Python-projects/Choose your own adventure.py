name = input("What is your name? ")
print(f"Welcome to the adventure, {name}!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right.Which way would you like to go ? ").lower()

if answer == "left":
    ans =input("You come to a river,you can walk around it or swim across ? type walk for walk around or swim for swim across.").lower
    if ans == "swim":
        print("Ohh no 🤦‍♂️ ,You swam across and were eaten by an alligator. ")
    elif ans == "walk":
        print("You walked for many miles , ran out of water and you lost the game")
    else :
        print("Not a valid option. You lose. ")

elif answer == "right":
    ans = input("You come to a bridge , it looks wobbly , do you wish to walk to cross it or head back (cross/back).").lower()

    if ans == "cross":
        ans = input("You crossed the bridge and came across a stranger. Do you wish to talk (yes/no) ").lower()
        
        if ans == "yes":
            print("You talk to the stranger.They gave you the gold and you won")
        elif ans == "no":
         print("You ignore the stranger.They got angry and stabbed you with a knife")
        else :
         print("Not a valid option. You lose. ")

    elif ans == "back":
        print("You go back and you lose")
    else :
        print("Not a valid option. You lose. ")


else:
   print("Not a valid option. You lose. ")

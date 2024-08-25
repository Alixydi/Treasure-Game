# Treasure Game
from art import logo2
print(logo2)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# First decision: left or right
choice1 = input('Do you want to go "left" or "right"? ').lower()

if choice1 == "left":
    # Second decision: swim or wait
    choice2 = input('Do you want to "swim" or "wait"? ').lower()

    if choice2 == "wait":
        # Third decision: which door
        choice3 = input('Which door? "Red", "Blue", or "Yellow"? ').lower()

        if choice3 == "yellow":
            print("You Win!")
        elif choice3 == "red":
            print("Burned by fire. Game Over.")
        elif choice3 == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("Fall into a hole. Game Over.")

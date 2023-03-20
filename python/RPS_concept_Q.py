# Suppose you are Game Engineer of a reputed IT Company and you need to develop a
# game for the company based on RPS; R-Rock, P-Paper and S-Scissors.
# Develop a game and lets the user play against computer.
# The program should work as follows:

# a. Display the options for the user to choose the based on the 1 for Rock, 2 for Paper
# and 3 for Scissors.
# b. For the computer user; create a function name ComputerRandomNumberGen() and
# that function generate a random number in the range 1 through 3 is generated.
# c. Create a function displayComputerChoice() for computer selection process and
# this function stored user rules based on:

# i. Case 1: R Selection:
# R has chosen when number is 1,
# ii. Case 2: P Selection:
# P has chosen when number is 2,
# iii. Case 3: S Selection:
# S has chosen when number is 3,

# d. Also store the user information name, address and phone number; when user win then
# display store information user name , address and phone has win the game on the file
# name inputData.txt with using any function.
# e. Create another function displayUserChoice()for the user choice and this
# function selection when user enters his/her choice among three RPS, at the keyboard.
# f. Then, computer’s choice is displayed.

# g. Create a function DetermineWinnerOfRPS() for determine the winner of the game
# taking two argument and winner is selected based to the following rules on the game:

# i. Case 1: R smashes S.
# If one player chooses rock and the other player chooses scissors, then rock will wins.
# ii. Case 2: S cuts P
# If one player chooses scissors and the other player chooses paper, then scissors will wins
# iii. Case 3: P wraps R
# If one player chooses paper and the other player chooses rock, then paper wins.
# iv. Case 4:
#  If User and Computer make the same choice
#  RPS game must be played again to determine the winner of RPS Game.

# h. Implement the result output through function display_static_Info() on the file
# name result.txt

import random

def ComputerRandomNumberGen():
    return random.randint(1, 3)

def displayComputerChoice(choice):
    if choice == 1:
        print("Computer has chosen R")
    elif choice == 2:
        print("Computer has chosen P")
    elif choice == 3:
        print("Computer has chosen S")

def displayUserChoice():
    choice = int(input("Enter your choice (1 for R, 2 for P, 3 for S): "))
    if choice == 1:
        print("You have chosen R")
    elif choice == 2:
        print("You have chosen P")
    elif choice == 3:
        print("You have chosen S")
    return choice

def DetermineWinnerOfRPS(user_choice, computer_choice):
    if user_choice == 1 and computer_choice == 3:
        return "User"
    elif user_choice == 2 and computer_choice == 1:
        return "User"
    elif user_choice == 3 and computer_choice == 2:
        return "User"
    elif user_choice == computer_choice:
        return "Tie"
    else:
        return "Computer"

def display_static_Info():
    with open("inputData.txt", "r") as f:
        data = f.read()
    with open("result.txt", "w") as f:
        f.write(data)

def main():
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone number: ")
    with open("inputData.txt", "w") as f:
        f.write(f"Name: {name}\nAddress: {address}\nPhone: {phone}\n")
    while True:
        user_choice = displayUserChoice()
        computer_choice = ComputerRandomNumberGen()
        displayComputerChoice(computer_choice)
        winner = DetermineWinnerOfRPS(user_choice, computer_choice)
        if winner == "User":
            print("Congratulations! You have won!")
            display_static_Info()
            break
        elif winner == "Computer":
            print("Sorry, you lost. Better luck next time!")
            break
        else:
            print("Tie! Play again.")

if __name__ == "__main__":
    main()

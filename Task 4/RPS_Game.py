# Task 4

import random
import os

moves_number = {
    0: "Rock",
    1: "Paper",
    2: "Scissors"
}

user_score = 0
computer_score = 0

while True:
    print()
    print(f"Your Score = {user_score}")
    print(f"Computers Score = {computer_score}")

    print()
    print("0 = Rock")
    print("1 = Paper")
    print("2 = Scissors")

    while True:
        try:
            print()
            user_move = int(input("Enter your move > "))
            if(user_move >= 0 and user_move <= 2):
                break
            else:
                print()
                print("Enter a number between 0-3!")
        except ValueError:
            print()
            print("Enter a number!")

    computer_move = random.randint(0, 2)

    print()
    print(f"Your Move = {moves_number[user_move]}")
    print(f"Computer's move = {moves_number[computer_move]}")

    if(
        user_move == 0 and computer_move == 2 or
        user_move == 2 and computer_move == 1 or
        user_move == 1 and computer_move == 0
    ):
        print()
        print("You Win!")
        user_score += 1

    elif(
        computer_move == 0 and user_move == 2 or
        computer_move == 2 and user_move == 1 or
        computer_move == 1 and user_move == 0
    ):
        print()
        print("Computer Wins!")
        computer_score += 1

    elif(
        user_move == computer_move
    ):
        print()
        print("Draw!")

    print()
    print("Play again?")
    while True:
        try:
            print()
            choice = int(input("0 = Yes | 1 = No > "))
            if(choice == 0 or choice == 1):
                break
            else:
                print()
                print("Enter either 0 or 1!")
        except ValueError:
            print()
            print("Enter a Number!")
            print()

    if(choice == 1):
        break

    os.system('clear')

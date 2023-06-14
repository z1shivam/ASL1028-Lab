import random

def roll_dice():
    return random.randint(1, 6)

def play_game():
    user_number = int(input("Guess a number between 1 and 6: "))
    computer_number = roll_dice()

    print("You rolled:", user_number)
    print("Computer rolled:", computer_number)

    if user_number > computer_number:
        print("Congratulations! You win!")
    elif user_number < computer_number:
        print("Sorry, the computer wins!")
    else:
        print("It's a tie!")

play_game()
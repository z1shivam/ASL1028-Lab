import random
user_input = int(input("Enter your choice:\n1. rock\n2. paper\n3. scissor\n\n"))
user_action = "0"
if user_input == 1: user_action = "rock"
if user_input == 2: user_action = "paper"
if user_input == 3: user_action = "scissors"



possible_actions = ["rock", "paper","scissors"]
computer_action =  random.choice(possible_actions)

print(f"\nYou choose {user_action}\ncomputer choose {computer_action}\n\n")

if user_action ==  computer_action:
    print("Its a tie")
elif user_action=="rock":
    if computer_action == "scissors":
        print("you winnnnnn!!!!!!!!!!!!!!")
    if computer_action == "paper":
        print("I won this time")
elif user_action == "paper":
    if computer_action == "rock":
        print("You won!!!")
    if computer_action == "scissors":
        print("i wonnnn!!!!")
elif user_action == "scissors":
    if computer_action == "rock":
        print("i Wonnn!!!!")
    if computer_action == "paper":
        print("You wonnnnnnnn")


import random
while True:
    user_action = input("Enter your choice (rock, paper, scissors):" )
    possible_action = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_action)
    print(f"You chose {user_action} and the computer chose {computer_action}.")

    if computer_action == user_action:
       print(f"Both players selected {user_action}")
    elif user_action == "rock":
       if computer_action == "scissors":
         print("Rock smashes scissors! You win")
    else:
        print("Paper covers rock! You lose!")

    elif user_action == "paper":
    if computer_action == "scissors":
        print("Scissors cut paper! You lose!")
    else:
        print("Paper covers rock! You win!")

elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cut paper! You lose!")
    else:
        print("Rock smashes scissors! You lose!")
play_again = input("Play again?(Y/N): ")

if play_again.lower() != "y":
    break
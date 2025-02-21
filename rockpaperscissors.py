import random
while True:
    play = input("Enter a choice (rock/paper/scissors): ")
    string = ["rock", "paper", "scissors"]
    computer = random.choice(string)
    if computer == play:
        print(f"This is a draw. You both selected {computer}")
    elif computer == "rock":
        if play == "paper":
            print(f"You win! The computer had chosen {computer}")
        else:
            print(f"Sorry you lost! The computer had chosen {computer}")
    elif computer == "paper":
        if play == "scissors":
            print(f"You win! The computer had chosen {computer}")
        else:
            print(f"Sorry, you lost! The computer had chosen {computer}")
    elif computer == "scissors":
        if play == "rock":
            print(f"You win! The computer had chosen {computer}")
        else:
            print(f"Sorry, you lost! The computer had chosen {computer}")
    playagain = input("Do you want to play again (y/n):")
    if playagain != "y":
        break
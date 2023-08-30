import random

while True:
    print("Enter your choice:\n1. Rock\n2. Paper\n3. Scissors\n")
    choice = int(input("User's turn: "))

    # Input validation
    while choice < 1 or choice > 3:
        choice = int(input("Invalid input. Please enter a number between 1 and 3: "))

    choices = ["Rock", "Paper", "Scissors"]
    choice_name = choices[choice - 1]

    print("User choice:", choice_name)
    print("Now it's the computer's turn...")

    computer_choice = random.randint(1, 3)
    computer_choice_name = choices[computer_choice - 1]

    print("Computer choice:", computer_choice_name)
    print(choice_name + " vs. " + computer_choice_name)

    if (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 1):
        print("Paper wins!")
        result = "Paper"
    elif (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 2):
        print("Scissors wins!")
        result = "Scissors"
    elif (choice == 1 and computer_choice == 3) or (choice == 3 and computer_choice == 1):
        print("Rock wins!")
        result = "Rock"
    else:
        result = "Tie"

    if result == choice_name:
        print("User wins!")
    elif result == computer_choice_name:
        print("Computer wins!")
    else:
        print("It's a tie!")

    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing the game!")

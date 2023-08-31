import random

def play_game():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock-Paper-Scissors Game!\n")
    
    rounds_to_play = int(input("Enter the number of rounds you want to play: "))
    
    for _ in range(rounds_to_play):
        print("Enter your choice:\n1. Rock\n2. Paper\n3. Scissors\n")
        choice = int(input("User's turn: "))

        while choice < 1 or choice > 3:
            choice = int(input("Invalid input. Please enter a number between 1 and 3: "))

        choices = ["Rock", "Paper", "Scissors"]
        choice_name = choices[choice - 1]

        print("User choice:", choice_name)
        print("Now it's computer's turn...")

        computer_choice = random.randint(1, 3)
        computer_choice_name = choices[computer_choice - 1]

        print("Computer choice:", computer_choice_name)
        print(choice_name + " vs. " + computer_choice_name)

        if (choice == 1 and computer_choice == 2) or (choice == 2 and computer_choice == 1):
            result = "Paper"

        elif (choice == 2 and computer_choice == 3) or (choice == 3 and computer_choice == 2):
            result = "Scissors"

        elif (choice == 1 and computer_choice == 3) or (choice == 3 and computer_choice == 1):
            result = "Rock"

        else:
            result = "Tie"

        if result == choice_name:
            print("User wins!")
            user_score += 1
        elif result == computer_choice_name:
            print("Computer wins!")
            computer_score += 1
        else:
            print("It's a tie!")

        print(f"User Score: {user_score}, Computer Score: {computer_score}")

    if user_score > computer_score :
        print("Congratulations! User wins the game..")
    elif user_score < computer_score:
        print(f"Sorry!! Better luck next time..")
    else :
        print("it's tie...")


while True:
    play_game()
    
    play_again = input("Do you want to play again? (Y/N): ")
    if play_again.lower() != 'y':
        break

print("Thanks for playing the game!")

import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
print("===== Rock Paper Scissors Game =====")
while True:
    print("\nChoose one:")
    print("rock")
    print("paper")
    print("scissors")

    user_choice = input("Enter your choice: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour Choice:", user_choice)
    print("Computer Choice:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Congratulations! You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
    print("\nScore")
    print("You:", user_score)
    print("Computer:", computer_score)
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
print("\n===== Final Score =====")
print("You:", user_score)
print("Computer:", computer_score)
print("Thank you for playing:)")

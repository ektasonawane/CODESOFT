import random
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"
user_score = 0
computer_score = 0
while True:
    print("\nRock, Paper, Scissors Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")
    user_choice = input("Enter your choice (1/2/3/4): ")
    if user_choice == '4':
        print("Final Scores:")
        print(f"You: {user_score} points")
        print(f"Computer: {computer_score} points")
        print("Thank you for playing!")
        break
    if user_choice not in ('1', '2', '3'):
        print("Invalid choice. Please select a valid option (1/2/3/4).")
        continue
    user_choice = int(user_choice)
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    user_choice_name = choices[user_choice]
    computer_choice = random.randint(1, 3)
    computer_choice_name = choices[computer_choice]
    print(f"\nYou chose: {user_choice_name}")
    print(f"Computer chose: {computer_choice_name}")
    result = determine_winner(user_choice_name, computer_choice_name)
    print(result)
    if result == "You win!":
        user_score += 1
    elif result == "Computer wins!":
        computer_score += 1
    print(f"Current Scores:")
    print(f"You: {user_score} points")
    print(f"Computer: {computer_score} points")
    play_again = input("Do you want to play another round? (yes/no): ")
    if play_again.lower() != "yes":
        print("Final Scores:")
        print(f"You: {user_score} points")
        print(f"Computer: {computer_score} points")
        print("Thank you for playing!")
        break
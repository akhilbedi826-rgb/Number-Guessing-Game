# Number Guessing Game
import random
from colorama import Fore, Style

print(Fore.LIGHTMAGENTA_EX + "\n===== Welcome to the Number Guessing Game =====" + Style.RESET_ALL)

def play_game():
    number = random.randint(1, 100)
    guess = 0
    attempts = 0

    while True:
        print("Choose the Difficulty: ")
        print("1 for Easy (12 attempts)")
        print("2 for Medium (7 attempts)")
        print("3 for Hard (5 attempts)")

        choice = input("Enter 1, 2 or 3: ")

        if (choice == "1"):
            max_attempts = 12
            break
        elif (choice == "2"):
            max_attempts = 7
            break
        elif (choice == "3"):
            max_attempts = 5
            break
        else:
            print(Fore.RED + "Invalid choice! Please Enter 1, 2, or 3" + Style.RESET_ALL)
            continue

    while True:
        if attempts >= max_attempts:
            print(Fore.RED + "You Lost!" + Style.RESET_ALL)
            print(Fore.RED + "You Have 0 Attempts Left" + Style.RESET_ALL)
            break

        try:
            guess = int(input("Guess the Number From 1 to 100: "))
        except ValueError:
            print(Fore.RED + "Please Enter Valid Number!" + Style.RESET_ALL)
            continue

        if guess > 100 or guess < 1:
            print(Fore.RED + "Please Enter number between 1 and 100 " + Style.RESET_ALL)
            continue

        attempts += 1

        if (guess < number):
            print(Fore.LIGHTYELLOW_EX + "GUESS HIGHER" + Style.RESET_ALL)
            print(f"You have {max_attempts - attempts} attempts left")

        elif (guess > number):
            print(Fore.LIGHTYELLOW_EX + "GUESS LOWER" + Style.RESET_ALL)
            print(f"You have {max_attempts - attempts} attempts left")

        else:
            print(Fore.GREEN + "Congratulations, You won" + Style.RESET_ALL)
            print(f"It took you {attempts} attempts out of {max_attempts} to guess the number.")
            break

while True:
    play_game()

    while True:  
        play_again = input("\nDo you want to play again? (y/yes or n/no): ").strip().lower()

        if play_again in ["y", "yes"]:
            break
        elif play_again in ["n", "no"]:
            print(Fore.BLUE + "\nThank you for playing! Goodbye " + Style.RESET_ALL)
            exit()
        else:
            print(Fore.RED + "Invalid input! Please type 'y/yes' or 'n/no'." + Style.RESET_ALL)

        




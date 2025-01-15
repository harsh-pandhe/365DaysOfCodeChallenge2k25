import random


def number_guessing_game():
    while True:
        print("\n--- New Game ---")
        lower = int(input("Enter the lower bound: "))
        upper = int(input("Enter the upper bound: "))
        number_to_guess = random.randint(lower, upper)
        attempts = 0

        while True:
            try:
                guess = int(input(f"Guess a number between {lower} and {upper}: "))
                attempts += 1

                if guess < number_to_guess:
                    print("Too low! Try again.")
                elif guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    print(f"🎉 Congrats! You guessed it in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


number_guessing_game()

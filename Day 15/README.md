# 🎯 Day #15 of My 365 Days Coding Challenge 2k25!  

---

## 💭 **A Personal Reflection:**  
Gaming is such a fun way to learn coding concepts! Today, I created a simple yet addictive **Number Guessing Game**, blending logic with interactivity. It’s amazing how something so straightforward can bring joy and sharpen problem-solving skills.  

---

## 📚 **What I Did Today:**  
I implemented a Python program where the user guesses a randomly generated number. The program gives hints like "Too high" or "Too low" to guide them, making it interactive and engaging.  

---

### Code:  

#### Basic Version:
```python
# number_guessing_game.py
import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
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

number_guessing_game()
```

#### Enhanced Version:
```python
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
```

---

## 💡 **Key Learning:**  
1. **Random Number Generation:** Using Python’s `random.randint` to create an unpredictable and exciting game.  
2. **Error Handling:** Utilizing `try-except` blocks to ensure smooth user input handling.  
3. **User Interaction:** Keeping the game engaging with helpful hints and dynamic gameplay.  

---

## ✨ **Extra Touch:**  
1. **Customizable Ranges:** Allowing the user to set their preferred range for the number guessing.  
2. **Replayability:** Adding an option to play multiple rounds without restarting the program.  
3. **High Score Tracking:** A potential future feature to display the best score (fewest attempts).  

---

## 🚀 **Your Turn:**  
- Extend the game to let the computer guess the user’s number using binary search logic.  
- Add a scoring system to track and display the highest score.  
- Implement a timer to measure how quickly a user guesses the number.  

---

#365DaysOfCode #CodingChallenge #NumberGuessingGame
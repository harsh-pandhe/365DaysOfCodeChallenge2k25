# 🎯 Day #2 of My 365 Days Coding Challenge 2k25!

---

## 💭 **A Personal Reflection:**

Today, I thought about how often we use calculators in our daily lives—quick math is something we all take for granted. But what if we could create one ourselves? This was the challenge for Day 2, and I realized coding is like building tools to solve our own problems.

---

## 📚 **What I Did Today:**

I created a simple calculator that can add, subtract, multiply, and divide two numbers. While it’s a basic program, it reminded me of the beauty of logic in programming. Also, I took it a step further by handling edge cases like division by zero.

---

### Code:

```python
# calculator.py
def calculator():
    print("Welcome to the Python Calculator! 🫮")
    num1 = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == '+':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif operation == '-':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif operation == '*':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif operation == '/':
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is undefined!")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")

calculator()
```

---

## 💡 **Key Learning:**

Writing even the simplest of programs teaches you to think like a problem-solver. It’s not just about the final output—it’s about thinking through every possibility and making your code robust.

---

## ✨ **Extra Touch:**

I added a little creativity to the user interface by making the calculator display its results in a fun, conversational style.

---

## 🚀 **Your Turn:**

If you were to design a calculator, what feature would you add to make it stand out? Drop your thoughts in the comments!

---

#365DaysOfCode #CodingChallenge #BuildYourTools


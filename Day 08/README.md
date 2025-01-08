# 🎯 Day #8 of My 365 Days Coding Challenge 2k25!

---

## 💭 **A Personal Reflection:**

Factorials remind me of how small actions can lead to exponential growth—like a single step that sparks a journey. Today, I took on the challenge of calculating factorials, a concept that’s as elegant in mathematics as it is in programming.

---

## 📚 **What I Did Today:**

I implemented a Python program to calculate the factorial of a number. Factorials are a foundational concept in math and have applications in everything from permutations to probability.

---

### Code:

#### Iterative Approach:
```python
# factorial.py
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print(f"The factorial of {num} is: {factorial(num)}")
```

#### Recursive Approach:
```python
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)
```

---

## 💡 **Key Learning:**

This task reinforced the importance of iteration and boundary cases. While the iterative method is simple and efficient, it’s fascinating to explore recursive approaches as well.

---

## ✨ **Extra Touch:**

I tested the program with different numbers, including edge cases like `0! = 1`. It’s amazing how such a small program can handle such a significant mathematical operation.

---

## 🚀 **Your Turn:**

Try implementing this using recursion or finding factorials for large numbers using libraries like `math.factorial`. What’s the largest number you’ve calculated the factorial for?

---

#365DaysOfCode #CodingChallenge #FactorialProgram

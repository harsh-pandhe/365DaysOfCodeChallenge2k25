# 🎯 Day #9 of My 365 Days Coding Challenge 2k25!

---

## 💭 **A Personal Reflection:**

Life is made up of small moments, just as numbers are made up of their digits. Today's challenge was all about breaking down a number into its parts and finding the sum. It's a reminder that even the smallest components contribute to the bigger picture.

---

## 📚 **What I Did Today:**

I wrote a Python program to calculate the sum of the digits in a number. Whether it’s for math puzzles or digital root calculations, this simple program has its charm.

---

### Code:

#### Iterative Approach:
```python
# sum_of_digits.py
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter a number: "))
print(f"The sum of the digits in {num} is: {sum_of_digits(num)}")
```

#### Handling Negative Numbers:
```python
# Modified for negative numbers
def sum_of_digits(n):
    n = abs(n)  # Handle negative numbers
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
```

#### One-Liner Approach:
```python
# Using list comprehension
def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))
```

---

## 💡 **Key Learning:**

This challenge reinforced the elegance of basic arithmetic. It also reminded me to handle edge cases, like negative numbers or zero. Exploring different approaches—iterative, modular, and one-liners—showed me how versatile Python can be.

---

## ✨ **Extra Touch:**

To add a creative spin, I explored the one-liner approach using `sum()` and `str()`. It’s amazing how concise and readable Python code can be while solving real-world problems.

---

## 🚀 **Your Turn:**

Try extending this to find the **digital root** of a number or sum the digits of multiple numbers in a list. What creative applications can you think of for this concept?

---

#365DaysOfCode #CodingChallenge #SumOfDigits
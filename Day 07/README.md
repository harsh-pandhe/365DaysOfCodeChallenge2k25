# 🎯 Day #7 of My 365 Days Coding Challenge 2k25!

---

## 💭 **A Personal Reflection:**

Life is full of swaps—changing roles, switching priorities, or even just rearranging your desk setup. Today’s challenge took this idea to code: swapping two variables without using a third. It’s a reminder that sometimes, you can achieve more with less if you think creatively.

---

## 📚 **What I Did Today:**

I wrote a Python program to swap two variables without relying on a third variable. It’s a clever use of arithmetic (or bitwise operators) to get the job done efficiently.

---

### Code:

#### Using Arithmetic Operations:
```python
# swap_variables.py
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

print(f"Before swap: a = {a}, b = {b}")

a = a + b
b = a - b
a = a - b

print(f"After swap: a = {a}, b = {b}")
```

#### Using XOR (Bitwise Operator):
```python
# Using XOR
a = a ^ b
b = a ^ b
a = a ^ b
```

---

## 💡 **Key Learning:**

This challenge showed me the power of simple arithmetic in problem-solving. By thinking outside the box, I avoided the need for extra memory and still achieved the desired result.

---

## ✨ **Extra Touch:**

For fun, I implemented an alternative approach using XOR (bitwise operator). It’s another efficient way to swap two variables without requiring a temporary variable.

---

## 🚀 **Your Turn:**

What’s your favorite way to swap variables without using extra space? Share your approach or try extending this idea to swap elements in a list!

---

#365DaysOfCode #CodingChallenge #SwapWithoutTemp
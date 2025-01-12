# 🎯 Day #12 of My 365 Days Coding Challenge 2k25!  

---

## 💭 **A Personal Reflection:**  
Finding common ground is a powerful skill, whether in teamwork or mathematics. Today, I tackled a challenge centered on harmony: calculating the **Least Common Multiple (LCM)** of two numbers. It’s about aligning numbers to their smallest shared rhythm—kind of poetic, isn’t it?  

---

## 📚 **What I Did Today:**  
I implemented a Python program to calculate the LCM of two numbers using the relationship between GCD (Greatest Common Divisor) and LCM.

---

### Code:

#### LCM for Two Numbers:
```python
# lcm.py
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
```

#### LCM for Multiple Numbers:
```python
from functools import reduce

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm_multiple(numbers):
    return reduce(lambda x, y: (x * y) // gcd(x, y), numbers)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
print(f"The LCM of {nums} is: {lcm_multiple(nums)}")
```

---

## 💡 **Key Learning:**  
This task reinforced how interconnected mathematical concepts are. By first understanding GCD, calculating LCM becomes straightforward and efficient.  

---

## ✨ **Extra Touch:**  
For fun, I extended the program to calculate the LCM of multiple numbers in a list. This addition showcases how a small tweak can make the program even more versatile and practical.

---

## 🚀 **Your Turn:**  

1. Modify this to handle more complex cases, like negative numbers or zero.  
2. Find the LCM of a large set of numbers and analyze the efficiency of your implementation.  

What’s the largest set of numbers you’ve calculated the LCM for?  

---

#365DaysOfCode #CodingChallenge #LCM  
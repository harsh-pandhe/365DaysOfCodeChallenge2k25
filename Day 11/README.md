# 🎯 Day #11 of My 365 Days Coding Challenge 2k25!  

---

## 💭 **A Personal Reflection:**  
Today’s challenge took me back to school math, where we learned about the **Greatest Common Divisor (GCD)**. It’s a simple yet powerful concept, teaching us how to find common ground—a great metaphor for teamwork and collaboration!

---

## 📚 **What I Did Today:**  

I wrote a Python function to find the GCD of two numbers using the **Euclidean algorithm**. It’s elegant, efficient, and a classic example of recursion.  

---

### Code:

#### Iterative Approach:
```python
# gcd.py
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")
```

#### Recursive Approach:
```python
# Recursive approach
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)
```

---

## 💡 **Key Learning:**  
This challenge taught me the elegance of the **Euclidean algorithm**. It’s fascinating how such a simple method can handle even large numbers efficiently.  

---

## ✨ **Extra Touch:**  
To take it a step further, I explored calculating the **Least Common Multiple (LCM)** using the GCD:  

```python
# Calculate LCM using GCD
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")
```

---

## 🚀 **Your Turn:**  

Try extending this concept:  
1. **Calculate LCM** for multiple numbers in a list.  
2. Experiment with GCD and LCM for negative numbers.  

What’s your favorite method for finding the GCD?  

---

#365DaysOfCode #CodingChallenge #GCD  
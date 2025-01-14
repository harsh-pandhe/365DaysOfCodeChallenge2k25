# 🎯 Day #14 of My 365 Days Coding Challenge 2k25!  

---

## 💭 **A Personal Reflection:**  
Exponentiation is like growth—small steps multiplied over time lead to big results. Today’s challenge was to calculate the power of a number using recursion, a method that reflects how problems can be broken down into smaller, solvable parts.  

---

## 📚 **What I Did Today:**  
I wrote a Python program that calculates the power of a number using recursion. Recursion is not just elegant—it’s also a great way to think about solving problems step by step.  

---

### Code:

#### Basic Power Function:
```python
# power_recursion.py
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exp} is: {power(base, exp)}")
```

#### Enhanced Version with Negative Exponent Handling:
```python
def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)
```

---

## 💡 **Key Learning:**  
This task was a great reminder of the importance of base cases in recursion. Without the `exp == 0` condition, the function could run indefinitely. I also learned how to handle edge cases like negative exponents, adding robustness to the solution.  

---

## ✨ **Extra Touch:**  
To make the program more versatile:  
- I added logic for handling negative exponents, ensuring accurate results for all inputs.  
- I explored comparisons with Python’s built-in `math.pow` for efficiency testing.  

---

## 🚀 **Your Turn:**  
1. Modify this program to calculate powers iteratively for better performance with large exponents.  
2. Compare the recursive approach with Python’s `math.pow` in terms of execution speed and ease of use.  
3. Try extending the program to compute modular exponentiation (useful in cryptography).  

What’s the most interesting use of recursion you’ve encountered?  

---

#365DaysOfCode #CodingChallenge #Recursion
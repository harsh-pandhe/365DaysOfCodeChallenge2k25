# 🎯 Day #4 of My 365 Days Coding Challenge 2k25!

---

## 💭 **A Personal Reflection:**

Have you ever thought about how unique prime numbers are? They’re like the “celebrities” of the number world—completely indivisible except by themselves and 1. Today’s challenge was about identifying these unique numbers, and it reminded me that even in code, simplicity can hide complexity.

---

## 📚 **What I Did Today:**

I wrote a Python program to check whether a given number is prime. This exercise wasn’t just about coding—it was about understanding the logical steps behind divisibility and efficiency in computation.

---

### Code:

```python
# prime_check.py
def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number! 🎉")
else:
    print(f"{num} is not a prime number. 🤔")
```

---

## 💡 **Key Learning:**

Prime numbers might seem simple at first glance, but they’ve been fascinating mathematicians and scientists for centuries. Writing this program taught me how to optimize logical checks to avoid unnecessary computations.

---

## ✨ **Extra Touch:**

To make it more interactive, I added prompts for user input and highlighted prime numbers with an exciting output message. Small touches can make programs more engaging!

---

## 🚀 **Your Turn:**

What’s the largest prime number you’ve ever come across? Or try modifying the code to find all primes in a range!

---

#365DaysOfCode #CodingChallenge #PrimeNumbers


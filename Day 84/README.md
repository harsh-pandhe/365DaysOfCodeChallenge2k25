# 🎯 Day #84 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today, I implemented the **Sieve of Eratosthenes**, a beautifully efficient algorithm for generating **prime numbers up to a given integer N**.
It’s fascinating how an idea from ancient mathematics still powers **modern applications** like **cryptography**, **hashing**, and **large-scale number theory problems**.

---

## 📚 What I Did Today

✅ Built a clean and efficient implementation of the **Sieve of Eratosthenes** in Python.
✅ Generated all prime numbers up to a given limit `n` in **O(n log log n)** time.
✅ Gained insights into how simple elimination can create powerful algorithms.

---

## 📝 Python Code – Sieve of Eratosthenes

```python
def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i in range(n + 1) if primes[i]]

n = 50
print(f"Prime numbers up to {n}:", sieve_of_eratosthenes(n))
```

---

## 💡 Key Learnings

✅ **Ancient idea, modern relevance**—used in RSA encryption, cryptographic hashing, prime testing, and numerical simulations.
✅ **Eliminates all multiples** of every found prime starting from `p²`.
✅ **Time Complexity:** O(n log log n)
✅ **Space Complexity:** O(n)

---

## 🚀 Your Turn

Try these enhancements:

* ✅ Implement the **Segmented Sieve** to handle `n` up to `10^12`.
* ✅ Use a **Bitset** or `bitarray` for **memory optimization**.
* ✅ Extend it to count prime gaps or twin primes.

---

\#365DaysOfCode #CodingChallenge #SieveOfEratosthenes #PrimeNumbers #MathAlgorithms #Cryptography #NumberTheory #Python

---
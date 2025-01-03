# 🎯 Day #3 of My 365 Days Coding Challenge 2k25!

---

## 💭 **A Personal Reflection:**

Patterns are everywhere—in nature, art, and even life itself. Today, I explored one of the most beautiful patterns in mathematics: the Fibonacci sequence. Seeing the sequence come alive through code felt like discovering the art hidden within logic.

---

## 📚 **What I Did Today:**

I wrote a Python program to calculate and display the first 10 Fibonacci numbers. The simplicity of the sequence (each number being the sum of the two before it) reminded me how powerful foundational concepts can be.

---

### Code:

```python
# fibonacci.py
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

fib_10 = fibonacci(10)
print("The first 10 Fibonacci numbers are:", fib_10)
```

---

## 💡 **Key Learning:**

The Fibonacci sequence is not just about numbers; it’s about understanding growth, patterns, and the beauty of recursion and iteration. Even simple loops can create something extraordinary!

---

## ✨ **Extra Touch:**

I created a visual output where the Fibonacci sequence builds step by step, like watching a story unfold. It’s fascinating to see how math and art intersect.

---

## 🚀 **Your Turn:**

What’s your favorite application of the Fibonacci sequence in the real world? (Hint: It’s everywhere, from flower petals to financial modeling!) Let’s discuss in the comments!

---

#365DaysOfCode #CodingChallenge #FibonacciSequence


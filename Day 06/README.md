# 🎯 Day #6 of My 365 Days Coding Challenge 2k25!

---

## 💭 **A Personal Reflection:**

They say the beauty of language lies in its vowels—they give words their rhythm and flow. Today’s challenge was about uncovering the hidden melody in a string by counting its vowels. This task reminded me how small things, like vowels in words, can have a significant impact.

---

## 📚 **What I Did Today:**

I wrote a Python program to count the number of vowels in a given string. It was a fun exercise in string traversal and condition checking.

---

### Code:

```python
# count_vowels.py
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count

user_string = input("Enter a string: ")
vowel_count = count_vowels(user_string)
print(f"The number of vowels in the string is: {vowel_count}")
```

---

## 💡 **Key Learning:**

This challenge taught me to think systematically. By iterating through the string and checking each character against a list of vowels, I saw how simple logic can produce powerful results.

---

## ✨ **Extra Touch:**

I tested the code with phrases like “Hello, World!” and even my name. It’s fascinating to see how vowel-heavy some words can be. For a twist, I might try extending this to count individual vowels or display their positions!

---

## 🚀 **Your Turn:**

Can you modify the program to count vowels and consonants separately? Or maybe count vowels in a sentence instead of a single word—go for it!

---

#365DaysOfCode #CodingChallenge #StringProcessing
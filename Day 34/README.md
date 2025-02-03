# 🎯 Day #34 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Have you ever noticed how **"listen"** and **"silent"** share the same letters but in a different order? That’s an **anagram**! Today, I worked on a fun challenge: **checking if two strings are anagrams.**  

## 📚 What I Did Today  
I implemented a Python program to determine whether two strings are **anagrams** (i.e., contain the same letters but arranged differently).  

### 🔹 Sorting-Based Approach  
A simple and efficient method using sorting:  

```python
# check_anagram.py
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

if are_anagrams(str1, str2):
    print("Yes! The strings are anagrams. ✅")
else:
    print("No! The strings are not anagrams. ❌")
```

## 💡 Key Learning  
- **Sorting Approach**: Sorting both strings and comparing them works in **O(n log n)** time complexity.  
- **Handling Edge Cases**:  
  - Ignoring spaces & case sensitivity ensures words like *"Dormitory"* and *"Dirty Room"* are detected as anagrams!  
  - Words with different lengths are immediately **not anagrams**.  

## ✨ Extra Touch  
### 🔹 Optimized Approach Using Frequency Count (O(n))  
A more efficient method using `Counter` from `collections`:  

```python
from collections import Counter

def are_anagrams(str1, str2):
    return Counter(str1) == Counter(str2)
```
This method is **faster** for large inputs!  

### 🔹 Edge Cases Considered  
- ✅ Words with different lengths (immediately return `False`).  
- ✅ Phrases with spaces (**"The Morse Code"** → **"Here come dots"**).  
- ✅ Anagrams with different letter cases (**"Heart"** = **"Earth"**).  

## 🚀 Your Turn  
Can you extend this to check for **multiple anagrams** in a list of words?  

---  

#365DaysOfCode #CodingChallenge #AnagramCheck  
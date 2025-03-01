# 🎯 Day #54 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever been in a crowded room where one person stands out? In a string, **the first non-repeating character** is like that one person—unique in a crowd! Today, I tackled this challenge using an efficient approach.  

## 📚 What I Did Today  
I wrote a function to find the **first non-repeating character** in a string. Instead of brute force, I used a **hashmap (dictionary) for O(n) efficiency!**  

### 📝 **Finding the First Non-Repeating Character**  

```python
from collections import Counter

def first_non_repeating_char(s):
    """Finds the first non-repeating character in a string."""
    char_count = Counter(s)  
    
    for char in s:
        if char_count[char] == 1:
            return char  
    
    return None 

s = "swiss"
result = first_non_repeating_char(s)
print("First non-repeating character:", result) 
```

## 💡 Key Learning  
- **Used `Counter` from collections** to store character frequencies.  
- **Single traversal to check for the first unique character**, keeping it **O(n)**.  
- **Works for any string length without excessive loops!**  

## ✨ Extra Touch  
✅ **Handles uppercase/lowercase properly (case-sensitive).**  
✅ **Returns `None` if all characters repeat.**  
✅ **Scalable for large strings.**  

## 🚀 Your Turn  
Modify this function to **return the index** of the first non-repeating character instead of the character itself!  

---

#365DaysOfCode #CodingChallenge #Python #StringManipulation  

# 🎯 Day #35 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever had a playlist with duplicate songs? Annoying, right? 😅 Today’s challenge was about **removing duplicate characters from a string**, keeping only the first occurrence.  

## 📚 What I Did Today  
I wrote a Python program that removes all duplicate characters while maintaining the original order.  

### 🔹 Set-Based Approach  
A simple and efficient way using a set:  

```python
# remove_duplicates.py
def remove_duplicates(string):
    seen = set()
    result = []
    
    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)
    
    return ''.join(result)

string = input("Enter a string: ")
print(f"String after removing duplicates: {remove_duplicates(string)}")
```

## 💡 Key Learning  
- **Using Sets for Uniqueness**: A set helps track seen characters efficiently.  
- **Preserving Order**: Unlike just using `set(string)`, this method **keeps** the original sequence.  

## ✨ Extra Touch  
### 🔹 Using `OrderedDict` for a One-Liner  
A more compact and elegant approach:  

```python
from collections import OrderedDict
def remove_duplicates(string):
    return ''.join(OrderedDict.fromkeys(string))
```
This approach is **shorter and more Pythonic**!  

### 🔹 Edge Cases Considered  
- ✅ Empty string (`""`).  
- ✅ Strings with all unique characters.  
- ✅ Strings with repeated characters (e.g., `"banana" → "ban"`).  

## 🚀 Your Turn  
Can you modify this to remove **duplicate words** instead of characters?  

---

#365DaysOfCode #CodingChallenge #RemoveDuplicates  
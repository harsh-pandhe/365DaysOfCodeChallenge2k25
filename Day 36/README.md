# 🎯 Day #36 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever tried to find similarities between words? Like how `"flight"`, `"flow"`, and `"flower"` all start with `"fl"`? 🌸 Today’s challenge was about finding the **Longest Common Prefix** in a list of strings.  

## 📚 What I Did Today  
I implemented a Python program that efficiently finds the **longest common prefix** among a list of words.  

### 🔹 Horizontal Scanning Approach  
This method iteratively trims the prefix until it matches all words.  

```python
# longest_common_prefix.py
def longest_common_prefix(words):
    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix

words = input("Enter words separated by spaces: ").split()
print(f"Longest Common Prefix: '{longest_common_prefix(words)}'")
```

## 💡 Key Learning  
- **Iterative Reduction**: Start with the first word and **trim** the prefix until it matches all words.  
- **Edge Cases**: If no common prefix exists, return an empty string (`""`).  

## ✨ Extra Touch  
### 🔹 Using `zip()` and `set()` for a Character-Wise Approach  
A more **efficient column-wise** method:  

```python
def longest_common_prefix(words):
    prefix = ""
    for chars in zip(*words):
        if len(set(chars)) == 1:
            prefix += chars[0]
        else:
            break
    return prefix
```
This method **compares characters column-wise**, stopping at the first mismatch.  

### 🔹 Edge Cases Considered  
- ✅ No words (`[]`) → Return `""`.  
- ✅ Completely different words (`["dog", "cat", "bird"]`) → Return `""`.  
- ✅ Identical words (`["hello", "hello", "hello"]`) → Return `"hello"`.  

## 🚀 Your Turn  
Can you modify this to find the **longest common suffix** instead?  

---

#365DaysOfCode #CodingChallenge #LongestCommonPrefix
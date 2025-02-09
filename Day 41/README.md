# 🎯 Day #41 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Have you ever tried remembering a long password without repeating characters? 🤯 That’s exactly the challenge I tackled today—finding the **longest substring without repeating characters**. This problem is a common **sliding window** technique used in interviews! 🚀  

## 📚 What I Did Today  
I implemented a **Sliding Window + HashSet** approach to efficiently find the longest unique substring in a given string.  

### 📝 **Longest Unique Substring Implementation**  

```python
# longest_unique_substring.py
def longest_unique_substring(s):
    char_set = set()
    left = max_length = 0  

    for right in range(len(s)):
        while s[right] in char_set:  
            char_set.remove(s[left])  
            left += 1  

        char_set.add(s[right])  
        max_length = max(max_length, right - left + 1)  

    return max_length  

strings = ["abcabcbb", "bbbbb", "pwwkew", "abcdef", "dvdf"]
for s in strings:
    print(f"'{s}' → {longest_unique_substring(s)}")
```

## 💡 Key Learning  
- **Sliding Window Technique:** Expands when a character is unique, contracts when a duplicate appears.  
- **Time Complexity:** **O(n)** (each character is visited at most twice).  
- **Edge Cases Considered:**  
  ✅ Empty string.  
  ✅ String with all unique characters.  
  ✅ String with all duplicate characters.  

## ✨ Extra Touch  
- ✅ **Optimized solution using a HashSet for quick lookups**  
- ✅ **Handles edge cases gracefully**  
- ✅ **Can be modified to return the actual substring, not just the length**  

## 🚀 Your Turn  
Modify this to **return the longest substring itself** instead of just the length!  

---

#365DaysOfCode #CodingChallenge #SlidingWindow  
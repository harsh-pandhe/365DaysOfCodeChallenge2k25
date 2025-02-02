# 🎯 Day #33 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever found duplicate songs in your playlist? Or duplicate names in your contact list? Today’s challenge was all about **finding duplicate elements in an array**, which is surprisingly useful in real-world scenarios like data cleaning and optimization.  

## 📚 What I Did Today  
I implemented a Python program to **detect duplicate elements** in an array using different approaches.  

### 🔹 Hashmap-Based Approach  
This method efficiently tracks duplicates in **O(n)** time complexity using a set:  

```python
# find_duplicates.py
def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
duplicates = find_duplicates(array)

print(f"Duplicate elements in the array: {duplicates}" if duplicates else "No duplicates found.")
```

## 💡 Key Learning  
- **Using Sets for Efficiency**: A set helps track seen elements in **O(n)** time complexity.  
- **Handling Edge Cases**: What if the array has **no duplicates**, or all elements are **duplicates**?  

## ✨ Extra Touch  
### 🔹 Using `Counter` from `collections`  
A more concise and Pythonic way to find duplicates:  

```python
from collections import Counter
def find_duplicates(arr):
    return [num for num, count in Counter(arr).items() if count > 1]
```

### 🔹 Edge Cases Considered  
- ✅ Empty array (`[]`).  
- ✅ Array with all unique elements.  
- ✅ Array where every element is a duplicate.  

## 🚀 Your Turn  
Can you modify this to **count the occurrences** of each duplicate? Or implement it without extra space?  

---  

#365DaysOfCode #CodingChallenge #FindDuplicates  
# 🎯 Day #67 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever wondered how many ways you can pick elements from a set? The concept of **subsets** is fundamental in combinatorics and is widely used in data science, dynamic programming, and even real-world decision-making! Today, I explored an **algorithm to generate all subsets of a given array** using recursion. 🚀  

## 📚 What I Did Today  
I implemented a **recursive approach** to find all subsets of a given array. The idea is simple:  
1. **Include** the current element in the subset and recurse.  
2. **Exclude** the current element and recurse.  

---

### 📝 **Subsets Generation Implementation**  

```python
def find_subsets(arr, index=0, current_subset=[]):
    if index == len(arr):
        print(current_subset)
        return
    
    find_subsets(arr, index + 1, current_subset)
    
    find_subsets(arr, index + 1, current_subset + [arr[index]])

arr = [1, 2, 3]
print("All subsets:")
find_subsets(arr)
```

---

## 💡 Key Learning  
✅ **How It Works:**  
- We **recursively explore** both possibilities—**including and excluding** each element.  
- When we reach the end of the array, we print the subset.  

✅ **Time Complexity:**  
- Since there are `2^n` possible subsets, the time complexity is **O(2^n)**.  

✅ **Why It’s Cool?**  
- **Used in AI & ML models for feature selection** 🤖  
- **Crucial for combinatorial problems & dynamic programming** 📊  
- **Forms the base of power set calculations** 🔥  

---

## ✨ Extra Touch  
🔍 **Real-World Applications:**  
- **Decision Trees in AI** 🏗  
- **Subset Sum Problems** 💰  
- **Finding combinations in recommendation systems** 🎵  

---

## 🚀 Your Turn  
Try modifying the code to **store subsets in a list** instead of printing them. Can you generate **only subsets of a specific size**? 🤔  

#365DaysOfCode #CodingChallenge #Recursion #Subsets #Backtracking  
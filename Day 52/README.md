# 🎯 Day #52 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Imagine having a row of numbered lockers, but one is missing. You could check each one manually, but what if there was a **faster way?** That’s today’s challenge—**finding the missing number in an array!**  

## 📚 What I Did Today  
I implemented a simple but **efficient** method using the **sum formula** to quickly identify the missing number in an array from `1 to N`.  

### 📝 **Finding the Missing Number Using the Sum Formula**  

```python
def find_missing_number(arr, n):
    """Find the missing number in an array from 1 to N"""
    expected_sum = n * (n + 1) // 2 
    actual_sum = sum(arr) 
    return expected_sum - actual_sum  

arr = [1, 2, 4, 5, 6] 
n = 6  
missing = find_missing_number(arr, n)
print("Missing Number:", missing)
```

## 💡 Key Learning  
- **Mathematical approach is O(1)** instead of iterating through the list.  
- **Uses the sum formula `N * (N + 1) / 2`** to determine the missing value.  
- **Works even if numbers aren’t in order!**  

## ✨ Extra Touch  
✅ **Efficient—no need for sorting or looping through missing values!**  
✅ **Handles large datasets in constant time!**  
✅ **Can be adapted for cases where multiple numbers are missing.**  

## 🚀 Your Turn  
Try modifying this function to **handle multiple missing numbers in an array!**  

---

#365DaysOfCode #CodingChallenge #MissingNumber #AlgorithmOptimization  

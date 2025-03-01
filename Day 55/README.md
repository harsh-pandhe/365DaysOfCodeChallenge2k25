# 🎯 Day #55 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Sorting is like **organizing a messy room**—sometimes, the simplest approach is to swap things around until everything falls into place! **Bubble Sort** is one of the easiest sorting algorithms to understand, yet it teaches fundamental concepts about **comparisons and swaps.**  

## 📚 What I Did Today  
I implemented **Bubble Sort**, a basic sorting algorithm that repeatedly **swaps adjacent elements** if they are in the wrong order. Although it’s not the most efficient, it’s a great way to learn about sorting!  

### 📝 **Bubble Sort Implementation**  

```python
def bubble_sort(arr):
    """Sorts an array using Bubble Sort algorithm."""
    n = len(arr)
    for i in range(n):
        swapped = False 
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break  

arr = [64, 25, 12, 22, 11]
print("Original Array:", arr)
bubble_sort(arr)
print("Sorted Array:", arr)
```

## 💡 Key Learning  
- **Optimized version**: If no swaps occur in a pass, the array is already sorted—**break early!**  
- **Time Complexity**: Worst-case **O(n²)**, but early termination helps in nearly sorted cases.  
- **Best used when array size is small or nearly sorted.**  

## ✨ Extra Touch  
✅ **Handles duplicate elements gracefully.**  
✅ **Added an optimization check (`swapped` flag).**  
✅ **Easily extendable to sort in descending order!**  

## 🚀 Your Turn  
Modify the function to **sort the array in descending order instead of ascending!**  

---

#365DaysOfCode #CodingChallenge #Sorting #BubbleSort #Python  
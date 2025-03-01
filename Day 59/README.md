# 🎯 Day #59 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Sorting algorithms are like problem-solving strategies—some take their time, while others **make smart choices and move quickly**. That’s **QuickSort** for you! It picks a **pivot**, divides the array, and conquers efficiently! 🚀  

## 📚 What I Did Today  
I implemented **QuickSort**, a **divide and conquer** algorithm that partitions an array around a pivot and sorts it **recursively**.  

### 📝 **QuickSort Implementation**  

```python
def quick_sort(arr):
    """Sorts an array using the QuickSort algorithm."""
    if len(arr) <= 1:
        return arr 

    pivot = arr[len(arr) // 2]  
    left = [x for x in arr if x < pivot]  
    middle = [x for x in arr if x == pivot]  
    right = [x for x in arr if x > pivot] 

    return quick_sort(left) + middle + quick_sort(right)  

arr = [10, 7, 8, 9, 1, 5]
print("Original Array:", arr)
sorted_arr = quick_sort(arr)
print("Sorted Array:", sorted_arr)
```

## 💡 Key Learning  
- **Concept**: Choose a pivot, partition elements, and recursively sort subarrays.  
- **Time Complexity**: **O(n log n) average**, but **O(n²) worst-case** if a bad pivot is chosen.  
- **Best used** when speed matters and random access is available (like in arrays).  

## ✨ Extra Touch  
✅ **Faster than Merge Sort in practice due to lower constant factors.**  
✅ **In-place version (Lomuto or Hoare partition) saves memory.**  
✅ **Used in real-world applications like database sorting.**  

## 🚀 Your Turn  
Try implementing **in-place QuickSort** using the **Lomuto partition scheme**!  

---

#365DaysOfCode #CodingChallenge #Sorting #QuickSort #Python  

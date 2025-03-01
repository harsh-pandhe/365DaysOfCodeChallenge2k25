# 🎯 Day #58 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Sorting can be slow, but what if we **divide and conquer**? That's the beauty of **Merge Sort**—it **splits** the array, sorts the halves, and merges them back **efficiently**! 🚀  

## 📚 What I Did Today  
I implemented **Merge Sort**, a recursive sorting algorithm that **divides** the array into smaller parts, sorts them, and **merges** them back in order.  

### 📝 **Merge Sort Implementation**  

```python

def merge_sort(arr):
    """Sorts an array using the Merge Sort algorithm."""
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]  

        merge_sort(left_half) 
        merge_sort(right_half)  

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = [38, 27, 43, 3, 9, 82, 10]
print("Original Array:", arr)
merge_sort(arr)
print("Sorted Array:", arr)
```

## 💡 Key Learning  
- **Concept**: Recursively splits the array, sorts the halves, and merges them.  
- **Time Complexity**: Always **O(n log n)**, making it **faster than Bubble, Selection, and Insertion Sort**.  
- **Best used** when **stable sorting** is required or when working with large datasets.  

## ✨ Extra Touch  
✅ **Works well for linked lists due to natural merging behavior.**  
✅ **Guaranteed O(n log n) performance.**  
✅ **Stable sorting (preserves order of equal elements).**  

## 🚀 Your Turn  
Try implementing **Merge Sort iteratively** instead of recursively!  

---

#365DaysOfCode #CodingChallenge #Sorting #MergeSort #Python  

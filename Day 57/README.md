# 🎯 Day #57 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Sorting is like **arranging playing cards in your hand**—you pick up each card and insert it in the correct position. **Insertion Sort** works in the same way! It builds a sorted section **one element at a time** by shifting elements into place.  

## 📚 What I Did Today  
I implemented **Insertion Sort**, which sorts an array by picking elements and placing them where they belong in the sorted portion.  

### 📝 **Insertion Sort Implementation**  

```python
def insertion_sort(arr):
    """Sorts an array using the Insertion Sort algorithm."""
    n = len(arr)

    for i in range(1, n):
        key = arr[i]  
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  

arr = [12, 11, 13, 5, 6]
print("Original Array:", arr)
insertion_sort(arr)
print("Sorted Array:", arr)
```

## 💡 Key Learning  
- **Concept**: Takes elements one by one and inserts them in the correct position.  
- **Time Complexity**: Worst-case **O(n²)**, but performs better on nearly sorted data.  
- **Best used** when data is **partially sorted** or for small datasets.  

## ✨ Extra Touch  
✅ **Works well with linked lists due to fewer swaps.**  
✅ **Efficient for small or nearly sorted arrays.**  
✅ **In-place sorting with no extra memory usage.**  

## 🚀 Your Turn  
Modify the function to **sort the array in descending order instead of ascending!**  

---

#365DaysOfCode #CodingChallenge #Sorting #InsertionSort #Python  

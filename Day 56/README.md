# 🎯 Day #56 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Sorting is like **choosing the best player for a team**—you look for the best candidate and place them in the right position. **Selection Sort** does exactly that by repeatedly selecting the smallest element and placing it in its correct position.  

## 📚 What I Did Today  
I implemented **Selection Sort**, an intuitive yet inefficient sorting algorithm that works by repeatedly **finding the minimum value** and swapping it into place.  

### 📝 **Selection Sort Implementation**  

```python
def selection_sort(arr):
    """Sorts an array using the Selection Sort algorithm."""
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):  
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [29, 10, 14, 37, 13]
print("Original Array:", arr)
selection_sort(arr)
print("Sorted Array:", arr)
```

## 💡 Key Learning  
- **Concept**: Finds the smallest element in each pass and places it at the start.  
- **Time Complexity**: Always **O(n²)** (not efficient for large datasets).  
- **Best used** when memory swaps are costly but comparisons are cheap.  

## ✨ Extra Touch  
✅ **Fewer swaps compared to Bubble Sort.**  
✅ **Easily extendable to descending order sorting.**  
✅ **No extra memory usage (in-place sorting).**  

## 🚀 Your Turn  
Modify the function to **sort the array in descending order instead of ascending!**  

---

#365DaysOfCode #CodingChallenge #Sorting #SelectionSort #Python  

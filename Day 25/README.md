## 🎯 Day #25 of My 365 Days Coding Challenge!  

---

### 💭 **A Personal Reflection:**  
Sorting arrays is an essential skill in programming. While it might appear basic, sorting forms the core of many algorithms and systems, from database queries to search engines. Today’s challenge reminded me of the joy of seeing chaos turned into order, one step at a time.  

---

### 📚 **What I Did Today:**  
I created a Python program to sort an array in ascending order. I explored both Python’s built-in `sorted()` function for simplicity and the manual implementation of the bubble sort algorithm for deeper understanding.  

---

### 🛠️ **Code:**  

#### Basic Sorting Using Built-in Function:  
```python
# sort_array.py
def sort_array(arr):
    return sorted(arr)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = sort_array(numbers)
print(f"Sorted array in ascending order: {sorted_numbers}")
```

#### Manual Sorting Using Bubble Sort:  
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = bubble_sort(numbers)
print(f"Sorted array in ascending order (manual): {sorted_numbers}")
```

---

### 💡 **Key Learning:**  
- Python’s `sorted()` function provides a quick and efficient way to sort arrays.  
- Implementing bubble sort helped me appreciate the logic behind sorting algorithms, even if they’re less efficient for large datasets.  
- Understanding sorting is foundational for optimizing real-world tasks involving large-scale data.  

---

### ✨ **Extra Touch:**  
- Added a manual implementation of bubble sort to reinforce algorithmic concepts.  
- Explored nested loops and array indexing, which are critical in manual sorting techniques.  

---

### 🚀 **Your Turn:**  
- Extend the program to sort arrays in descending order.  
- Modify it to handle arrays of strings or mixed data types.  
- Implement and compare other sorting algorithms like insertion sort or quicksort.  

---

#365DaysOfCode #CodingChallenge #Sorting  
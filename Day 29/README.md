## 🎯 Day #29 of My 365 Days Coding Challenge!  

---

### 💭 **A Personal Reflection:**  
Searching for something is part of life, whether it’s finding a key in your bag or a value in an array. Today’s challenge took me back to the basics with **linear search**—a fundamental yet powerful algorithm for its simplicity.  

---

### 📚 **What I Did Today:**  
I implemented a Python program to perform a **linear search** on an array. This method sequentially checks each element until it finds the desired value or determines it’s not there.  

---

### 🛠️ **Code:**  

```python
# linear_search.py
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
target = int(input("Enter the target value to search: "))

result = linear_search(array, target)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found in the array.")
```  

---

### 💡 **Key Learning:**  
- Linear search may not be the fastest algorithm for large datasets, but it’s effective for unsorted or small arrays.  
- It’s the most straightforward search method, useful for understanding more complex search algorithms like binary search.  
- Breaking a problem into small, manageable steps always simplifies the process.  

---

### ✨ **Extra Touch:**  
- Added functionality to return **all indices** where the target value occurs (to handle duplicates).  
- Enhanced user experience by improving input prompts and output clarity.  

---

### 🚀 **Your Turn:**  
- Modify the program to work with **strings** (e.g., searching for substrings in a list).  
- Extend the logic to handle **2D arrays** or **nested lists**.  
- Implement an optimization to stop the search early if the array is sorted.  

---

#365DaysOfCode #CodingChallenge #LinearSearch
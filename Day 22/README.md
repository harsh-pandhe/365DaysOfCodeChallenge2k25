## 🎯 Day #22 of My 365 Days Coding Challenge!  

---

### 💭 **A Personal Reflection:**  
Arrays are the backbone of many algorithms, and today’s challenge was about something fundamental yet crucial—summing up all the elements in an array. It reminded me how even simple operations form the foundation of more complex programs.  

---

### 📚 **What I Did Today:**  
I implemented a Python program to calculate the sum of elements in an array. The task focused on efficiency, clarity, and exploring different approaches to achieve the same goal.  

---

### 🛠️ **Code:**  

#### Using Python's Built-in `sum()` Function:  
```python
# sum_of_array.py
def sum_of_array(arr):
    return sum(arr)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = sum_of_array(numbers)
print(f"The sum of the array elements is: {result}")
```

#### Manual Approach Using Loops:  
```python
def sum_of_array_manual(arr):
    total = 0
    for num in arr:
        total += num
    return total

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = sum_of_array_manual(numbers)
print(f"The sum of the array elements is: {result}")
```

---

### 💡 **Key Learning:**  
- Python’s built-in functions like `sum()` simplify operations, but understanding manual implementations is equally important for coding in low-level environments.  
- Loops provide flexibility for custom operations, like filtering specific elements (e.g., even or odd numbers).  

---

### ✨ **Extra Touch:**  
I explored a manual approach to summing the array elements and set up the foundation for extending the program to handle specific tasks, like summing even or odd numbers.

---

### 🚀 **Your Turn:**  
- Modify this program to calculate the sum of only even or odd numbers in an array.  
- Extend the program to handle arrays of floating-point numbers.  

---

#365DaysOfCode #CodingChallenge #SumOfArray  
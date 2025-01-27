## 🎯 Day #28 of My 365 Days Coding Challenge!  

---

### 💭 **A Personal Reflection:**  
Finding the median can feel like walking a tightrope between the extremes. It’s a middle point that balances the entire dataset, and today’s challenge reminded me how important it is in statistics and real-world data analysis.

---

### 📚 **What I Did Today:**  
I wrote a Python function to find the median of a set of numbers. The median is the middle value when the numbers are sorted.

---

### 🛠️ **Code:**  

```python
# find_median.py
def find_median(numbers):
    numbers.sort()
    n = len(numbers)
    
    if n % 2 != 0:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
median = find_median(numbers)
print(f"The median is: {median}")
```

---

### 💡 **Key Learning:**  
- Sorting is essential when calculating the median.
- Handling both even and odd sets of data ensures correctness and robustness.

---

### ✨ **Extra Touch:**  
I modified the function to handle more edge cases, such as an empty list or invalid input:

```python
def find_median_safe(numbers):
    if not numbers:
        return "Input list is empty!"
    numbers.sort()
    n = len(numbers)
    if n % 2 != 0:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
median = find_median_safe(numbers)
print(f"The median is: {median}")
```

---

### 🚀 **Your Turn:**  
- Modify the program to find the median in a stream of incoming numbers (without storing the entire list).

---

#365DaysOfCode #CodingChallenge #Median
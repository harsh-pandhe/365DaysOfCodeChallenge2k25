# 🎯 Day #17 of My 365 Days Coding Challenge!  

---

## 💭 **A Personal Reflection:**  
Some decisions are tough, like choosing the best out of three options. Thankfully, coding makes it simpler when it comes to numbers! Today, I tackled a challenge to find the largest of three numbers using conditional logic.  

---

## 📚 **What I Did Today:**  
I wrote a Python program to take three numbers as input and determine the largest. This is a great task for practicing comparisons and logical operators.  

---

### Code:  

```python
# largest_of_three.py
def find_largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
largest = find_largest(num1, num2, num3)
print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
```

---

## 💡 **Key Learning:**  
This task was a great exercise in understanding **if-elif-else** structures. It also highlighted how proper input validation and logic make programs more robust.  

---

## ✨ **Extra Touch:**  
To make the program more dynamic, I extended it to handle any number of inputs:  

```python
def find_largest_in_list(numbers):
    return max(numbers)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
largest = find_largest_in_list(nums)
print(f"The largest number in the list {nums} is: {largest}")
```

---

## 🚀 **Your Turn:**  
- Can you write a version of this program without using conditional statements or built-in functions like `max`?  
- Hint: Try using sorting!  

---

#365DaysOfCode #CodingChallenge #LargestNumber  
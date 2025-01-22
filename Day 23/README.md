## 🎯 Day #23 of My 365 Days Coding Challenge!  

---

### 💭 **A Personal Reflection:**  
Armstrong numbers are like little puzzles—they look simple, but there’s elegance in how they are formed. Solving this challenge was a reminder of how breaking down a problem into smaller, manageable steps makes even complex tasks approachable.  

---

### 📚 **What I Did Today:**  
I wrote a Python program to determine if a number is an Armstrong number. This involved extracting the digits of the number, calculating the power of each digit, and summing these powers to check against the original number.  

---

### 🛠️ **Code:**  

#### Checking if a Number is Armstrong:  
```python
# armstrong_number.py
def is_armstrong(number):
    digits = list(map(int, str(number)))
    power = len(digits)
    return sum(digit ** power for digit in digits) == number

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number!")
else:
    print(f"{num} is not an Armstrong number.")
```

#### Finding All Armstrong Numbers in a Range:  
```python
def find_armstrong_numbers(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
armstrong_numbers = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")
```

---

### 💡 **Key Learning:**  
- Armstrong numbers are an excellent example of how mathematical concepts can be applied programmatically.  
- The task reinforced the importance of using loops, list comprehensions, and mathematical operations effectively.  
- Python’s ability to handle large numbers without overflow is immensely helpful for such challenges.  

---

### ✨ **Extra Touch:**  
I extended the program to find all Armstrong numbers within a given range, making it more dynamic and useful for exploring this concept further.  

---

### 🚀 **Your Turn:**  
- Extend this program to check for Armstrong numbers in other numeral systems like binary or hexadecimal.  
- Modify it to handle inputs with multiple ranges simultaneously.  

---

#365DaysOfCode #CodingChallenge #ArmstrongNumber  
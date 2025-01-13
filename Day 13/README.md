# 🎯 Day #13 of My 365 Days Coding Challenge 2k25!  

---

## 💭 **A Personal Reflection:**  
Multiplication tables were my first introduction to math patterns as a child. They’re simple, repetitive, and foundational—just like coding basics. Today, I revisited those nostalgic memories by creating a program to generate a multiplication table for any given number.  

---

## 📚 **What I Did Today:**  
I wrote a Python program that generates a neat and customizable multiplication table. It’s a great way to practice loops and formatting.  

---

### Code:

#### Basic Multiplication Table:
```python
# multiplication_table.py
def multiplication_table(num, up_to=10):
    print(f"Multiplication Table for {num}:")
    for i in range(1, up_to + 1):
        print(f"{num} x {i} = {num * i}")

number = int(input("Enter the number for the multiplication table: "))
limit = int(input("Enter how far you want the table to go: "))
multiplication_table(number, limit)
```

#### Pretty-Formatted Multiplication Table:
```python
def multiplication_table_pretty(num, up_to=10):
    print(f"--- Multiplication Table for {num} ---")
    for i in range(1, up_to + 1):
        print(f"| {num} x {i:2} | {num * i:3} |")
    print("-" * 30)
```

---

## 💡 **Key Learning:**  
This task highlighted the power of iteration and formatting in programming. It’s also a reminder of how even basic programs can be adapted to suit different needs.  

---

## ✨ **Extra Touch:**  
I made the table more visually appealing by adding formatting and borders. It not only looks better but also makes it easier to read and understand.  

---

## 🚀 **Your Turn:**  
1. Extend this program to generate tables for multiple numbers simultaneously.  
2. Export the multiplication tables to a text or CSV file for sharing or documentation.  
3. Create interactive tables in a graphical interface for added user engagement.  

What’s the most creative use of a multiplication table you can think of?  

---

#365DaysOfCode #CodingChallenge #MultiplicationTable  
# 🎯 Day #38 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Stacks are everywhere! From the **undo** button in your favorite app to the way we navigate web pages using the **back button**. Today, I implemented a **stack using an array**, one of the most fundamental data structures.  

## 📚 What I Did Today  
I built a **custom stack** using Python’s list, handling `push`, `pop`, `peek`, and checking if the stack is empty.  

### 🔹 Stack Implementation Using an Array  

```python
# stack_array.py
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        """Push an element onto the stack."""
        self.stack.append(value)
        print(f"Pushed {value}")

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        """Return the top element without removing it."""
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.stack) == 0

    def display(self):
        """Print the stack elements."""
        print("Stack:", self.stack[::-1])

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()
print(f"Popped: {stack.pop()}")
print(f"Top Element: {stack.peek()}")
stack.display()
```

## 💡 Key Learning  
- **LIFO (Last-In-First-Out)**: The last element pushed is the first to be popped.  
- **Time Complexity**:  
  - `push()`: **O(1)** (appending to the end of the list)  
  - `pop()`: **O(1)** (removing from the end)  
  - `peek()`: **O(1)**  
  - `is_empty()`: **O(1)**  

## ✨ Extra Touch  
### 🔹 Handling Stack Overflow & Underflow (for fixed-size stacks)  
To prevent pushing beyond a fixed limit:  

```python
def __init__(self, capacity):
    self.stack = []
    self.capacity = capacity

def push(self, value):
    if len(self.stack) < self.capacity:
        self.stack.append(value)
    else:
        print("Stack Overflow!")
```

### 🔹 Edge Cases Considered  
✅ Trying to `pop()` from an empty stack.  
✅ Peeking when the stack is empty.  
✅ Handling large inputs efficiently.  

## 🚀 Your Turn  
Can you modify this to use a **linked list instead of an array**?  

---

#365DaysOfCode #CodingChallenge #StackImplementation  
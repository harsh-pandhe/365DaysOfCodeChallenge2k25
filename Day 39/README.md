# 🎯 Day #39 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever stood in a queue waiting for your turn? That’s exactly how a **queue** works in programming! **First In, First Out (FIFO)** is the rule, just like waiting in line for coffee ☕. Today, I implemented a **queue using an array** to reinforce this concept.  

## 📚 What I Did Today  
I built a **custom queue** using Python’s list, supporting `enqueue`, `dequeue`, `peek`, and checking if the queue is empty.  

### 📝 Queue Implementation Using an Array  

```python
# queue_array.py
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        """Add an element to the end of the queue."""
        self.queue.append(value)
        print(f"Enqueued {value}")

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if not self.is_empty():
            return self.queue.pop(0)
        return "Queue is empty"

    def peek(self):
        """Return the front element without removing it."""
        if not self.is_empty():
            return self.queue[0]
        return "Queue is empty"

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def display(self):
        """Print the queue elements."""
        print("Queue:", self.queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()
print(f"Dequeued: {queue.dequeue()}")
print(f"Front Element: {queue.peek()}")
queue.display()
```

## 💡 Key Learning  
- **FIFO (First-In-First-Out):** The first element enqueued is the first to be dequeued.  
- **Time Complexity:**  
  - `enqueue()`: **O(1)** (appending to the list)  
  - `dequeue()`: **O(n)** (removing from the front, shifting elements)  
  - `peek()`: **O(1)**  
  - `is_empty()`: **O(1)**  

## ✨ Extra Touch  
### 🔹 Optimizing `dequeue()` Using `collections.deque` (O(1) Instead of O(n))  
To prevent shifting elements when dequeuing, we can use `collections.deque`:  

```python
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        return self.queue.popleft() if self.queue else "Queue is empty"
```

### 🔹 Edge Cases Considered  
✅ Dequeuing from an empty queue.  
✅ Peeking when the queue is empty.  
✅ Handling large inputs efficiently.  

## 🚀 Your Turn  
Can you modify this to use a **circular queue** instead of a simple array?  

---

#365DaysOfCode #CodingChallenge #QueueImplementation  
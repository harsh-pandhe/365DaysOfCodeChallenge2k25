# 🎯 Day #49 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Stacks are like a **last-in, first-out (LIFO)** buffet—**the last plate you put on top is the first one you take!** But what if you only had **queues** (which follow FIFO: first-in, first-out) to implement a stack? 🤯  

## 📚 What I Did Today  
I implemented a **stack using two queues**! Even though **queues work differently**, with the right approach, we can mimic **LIFO behavior** efficiently.  

### 📝 **Stack Implementation Using Two Queues**  

```python
# stack_using_queues.py
from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """ Push an element onto the stack """
        self.queue1.append(x)

    def pop(self):
        """ Removes the top element from the stack """
        if not self.queue1:
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        top_element = self.queue1.popleft()
        
        self.queue1, self.queue2 = self.queue2, self.queue1  
        
        return top_element

    def top(self):
        """ Returns the top element without removing it """
        if not self.queue1:
            return None
        
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        top_element = self.queue1.popleft()
        self.queue2.append(top_element)
        
        self.queue1, self.queue2 = self.queue2, self.queue1  
        
        return top_element

    def is_empty(self):
        """ Checks if the stack is empty """
        return len(self.queue1) == 0

stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)

print("Top element:", stack.top())
print("Popped element:", stack.pop())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())
print("Popped element:", stack.pop())
print("Is stack empty?", stack.is_empty())
```

## 💡 Key Learning  
- **Push is O(1), but pop is O(n)** since we have to shift elements between queues.  
- **Queues follow FIFO, so we move elements to preserve LIFO behavior.**  
- **We can optimize further by making either `push()` or `pop()` more efficient!**  

## ✨ Extra Touch  
✅ **Implements stack behavior with only queues**  
✅ **Uses `deque` for efficient queue operations**  
✅ **Can be modified to optimize push instead of pop**  

## 🚀 Your Turn  
Try implementing **a stack using just one queue** instead of two!  

---

#365DaysOfCode #CodingChallenge #StackVsQueue #DataStructures  
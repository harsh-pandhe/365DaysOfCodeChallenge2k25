# 🎯 Day #50 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Queues are like standing in line for coffee ☕—**first person in, first person out (FIFO).** But what if you only had **stacks**, which work in **LIFO (last-in, first-out) order?** That’s today’s challenge!  

## 📚 What I Did Today  
I implemented a **queue using two stacks**. Even though stacks and queues operate differently, we can still achieve FIFO behavior with some clever manipulation!  

### 📝 **Queue Implementation Using Two Stacks**  

```python
# queue_using_stacks.py
class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        """ Push element to the end of the queue """
        self.stack1.append(x)

    def dequeue(self):
        """ Remove and return the front element of the queue """
        if not self.stack1 and not self.stack2:
            return None
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def front(self):
        """ Get the front element without removing it """
        if not self.stack1 and not self.stack2:
            return None
        
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def is_empty(self):
        """ Check if the queue is empty """
        return not self.stack1 and not self.stack2

queue = QueueUsingStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Front element:", queue.front())
print("Dequeued element:", queue.dequeue())
print("Dequeued element:", queue.dequeue())
print("Is queue empty?", queue.is_empty())
print("Dequeued element:", queue.dequeue())
print("Is queue empty?", queue.is_empty())
```

## 💡 Key Learning  
- **Enqueue is O(1), but dequeue is O(n) when transferring elements.**  
- **Using two stacks helps reverse the LIFO behavior of stacks into FIFO for queues.**  
- **Can be optimized to make either enqueue or dequeue more efficient!**  

## ✨ Extra Touch  
✅ **Mimics queue behavior using only stacks**  
✅ **Efficient for multiple enqueues before a dequeue**  
✅ **Can be optimized for different use cases**  

## 🚀 Your Turn  
Try modifying this so that **dequeue is O(1) instead of O(n)!**  

---

#365DaysOfCode #CodingChallenge #QueueVsStack #DataStructures  
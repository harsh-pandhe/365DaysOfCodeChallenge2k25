# 🎯 Day #46 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever been stuck in a **never-ending loop** of thoughts? Well, that’s kinda like a **circular queue**—where the last element connects back to the first! 🔄 Today, I implemented a **Circular Queue**, which is super useful in scheduling, buffering, and more!  

## 📚 What I Did Today  
I created a **fixed-size circular queue** using an array. It supports **enqueue, dequeue, peek, and isEmpty/isFull operations** in **O(1) time**!  

### 📝 **Circular Queue Implementation**  

```python
# circular_queue.py
class CircularQueue:
    def __init__(self, k):
        self.queue = [None] * k
        self.size = k
        self.front = self.rear = -1

    def enqueue(self, value):
        if self.isFull():
            print("Queue is full! 🚫")
            return
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value
        print(f"Enqueued: {value} ✅")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty! ❌")
            return
        print(f"Dequeued: {self.queue[self.front]} 🔄")
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size

    def peek(self):
        return None if self.isEmpty() else self.queue[self.front]

    def isEmpty(self):
        return self.front == -1

    def isFull(self):
        return (self.rear + 1) % self.size == self.front

    def display(self):
        if self.isEmpty():
            print("Queue is empty! 🚀")
            return
        index = self.front
        print("Queue elements: ", end="")
        while index != self.rear:
            print(self.queue[index], end=" <- ")
            index = (index + 1) % self.size
        print(self.queue[self.rear])

cq = CircularQueue(5)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.display()
cq.dequeue()
cq.enqueue(60)
cq.display()
print("Front element:", cq.peek())
```

## 💡 Key Learning  
- Circular queues **prevent memory wastage** compared to normal queues.  
- **Modulo operation (`%`)** is used to wrap around the indices.  
- **Time Complexity:** **O(1)** for all operations.  

## ✨ Extra Touch  
✅ **Handles wrap-around scenarios seamlessly**  
✅ **Prevents overflow & underflow conditions**  
✅ **Can be extended for a dynamic circular queue**  

## 🚀 Your Turn  
Try implementing this **using a Linked List** instead of an array!  

---

#365DaysOfCode #CodingChallenge #DataStructures  
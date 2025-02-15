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

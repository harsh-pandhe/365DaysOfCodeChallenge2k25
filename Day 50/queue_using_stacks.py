class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, x):
        """Push element to the end of the queue"""
        self.stack1.append(x)

    def dequeue(self):
        """Remove and return the front element of the queue"""
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()

    def front(self):
        """Get the front element without removing it"""
        if not self.stack1 and not self.stack2:
            return None

        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1]

    def is_empty(self):
        """Check if the queue is empty"""
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

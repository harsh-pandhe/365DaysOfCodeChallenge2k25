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

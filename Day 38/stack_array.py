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

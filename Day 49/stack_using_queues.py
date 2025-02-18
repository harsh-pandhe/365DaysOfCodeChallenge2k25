from collections import deque


class StackUsingQueues:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """Push an element onto the stack"""
        self.queue1.append(x)

    def pop(self):
        """Removes the top element from the stack"""
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        top_element = self.queue1.popleft()

        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def top(self):
        """Returns the top element without removing it"""
        if not self.queue1:
            return None

        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        top_element = self.queue1.popleft()
        self.queue2.append(top_element)

        self.queue1, self.queue2 = self.queue2, self.queue1

        return top_element

    def is_empty(self):
        """Checks if the stack is empty"""
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

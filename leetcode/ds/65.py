# stack from scratch

class Stack:
    def __init__(self):
        self.stack = []

    # Add element to top
    def push(self, val):
        self.stack.append(val)

    # Remove and return top element
    def pop(self):
        if self.is_empty():
            return None

        return self.stack.pop()

    # Return top element without removing
    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    # Check whether stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Return number of elements
    def size(self):
        return len(self.stack)


# Example
stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print(stack.stack)      # [10, 20, 30]
print(stack.peek())     # 30
print(stack.pop())      # 30
print(stack.pop())      # 20
print(stack.peek())     # 10
print(stack.size())     # 1
print(stack.is_empty()) # False
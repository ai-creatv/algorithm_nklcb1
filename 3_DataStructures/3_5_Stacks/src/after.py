import array

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = 0
        self.array = array.array('l', [0]*capacity)
    
    def push(self, value):
        if self.capacity == self.top:
            return False
        else:
            self.array[self.top] = value
            self.top += 1
            return True

    def pop(self):
        if self.top == 0:
            return None
        else:
            self.top -= 1
            return self.array[self.top]
    
    def peek(self):
        if self.top == 0:
            return None
        else:
            return self.array[self.top - 1]
    
    def is_empty(self):
        return self.top == 0

    def print(self):
        print(self.array.tolist()[:self.top])


stack = Stack(4)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print()

stack.push(5)
stack.print()

print(stack.pop())
print(stack.pop())
stack.print()

print(stack.peek())
stack.print()

print(stack.pop())
print(stack.pop())
print(stack.pop())
stack.print()

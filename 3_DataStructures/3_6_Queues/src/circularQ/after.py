import array

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.is_full = False
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.is_full is True:
            return False
        
        self.array[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity

        if self.front == self.rear:
            self.is_full = True
        return True

    def get(self):
        if self.is_full is False and self.front == self.rear:
            return None
        
        self.is_full = False
        
        value = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        return value

    def peek(self):
        if self.is_full is False and self.front == self.rear:
            return None
        
        return self.array[self.front]
        
    def print(self):
        if self.rear == self.front and self.is_full is False:
            print('[]')
            return

        start = self.front
        end = self.rear
        if self.rear <= self.front:
            end += self.capacity
        
        s = '['
        for i in range(start, end):
            s += str(self.array[i % self.capacity]) + ' '
        s += ']'
        print(s)


queue = CircularQueue(5)
queue.print()

queue.put(1)
queue.put(2)
queue.put(3)
queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
print(queue.get())
queue.print()

queue.put(4)
queue.put(5)
queue.put(6)
queue.print()

print(queue.get())
print(queue.get())
print(queue.get())
queue.print()
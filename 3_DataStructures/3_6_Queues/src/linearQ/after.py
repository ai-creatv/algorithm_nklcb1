import array

class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        if self.rear == self.capacity:
            print('queue overflow')
            return False
        
        self.array[self.rear] = value
        self.rear += 1
        return True

    def get(self):
        if self.front == self.rear:
            print('queue underflow')
            return None
    
        value = self.array[self.front]
        self.front += 1
        return value

    def peek(self):
        if self.front == self.rear:
            return None
        return self.array[self.front]

    def print(self):
        if self.front == self.rear:
            print('[]')
        else:
            print('[', end='')
            for i in range(self.front, self.rear - 1):
                print(self.array[i], end=', ')
            print(str(self.array[self.rear - 1]) + ']')


queue = LinearQueue(5)
queue.print()

queue.put(1)
queue.put(2)
queue.put(3)
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
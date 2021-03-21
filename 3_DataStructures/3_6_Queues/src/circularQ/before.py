import array

class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = 0
        self.rear = 0
        self.array = array.array('l', [0]*capacity)

    def put(self, value):
        pass

    def get(self):
        pass

    def peek(self):
        pass

    def print(self):
        pass

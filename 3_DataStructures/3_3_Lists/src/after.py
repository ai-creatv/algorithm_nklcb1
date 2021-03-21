import array

class ArrayList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.length = 0
        self.array = array.array('l', [0]*capacity)
    
    def is_empty(self):
        return self.capacity == 0

    def prepend(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                new_array[i + 1] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length - 1, -1, -1):
                self.array[i + 1] = self.array[i]

        self.array[0] = value
        self.length += 1

    def append(self, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(self.length):
                new_array[i] = self.array[i]
            self.array = new_array
        
        self.array[self.length] = value
        self.length += 1

    def set_head(self, index):
        self.array = self.array[index:]
        self.capacity = self.capacity - index
        self.length = self.length - index

    def access(self, index):
        return self.array[index]

    def insert(self, index, value):
        if self.capacity == self.length:
            self.capacity *= 2
            new_array = array.array('l', [0]*self.capacity)
            for i in range(index, self.length):
                new_array[i] = self.array[i]
            self.array = new_array
        else:
            for i in range(self.length - 1, index - 1, -1):
                self.array[i + 1] = self.array[i]

        self.array[index] = value
        self.length += 1

    def remove(self, index):
        for i in range(index, self.length - 1):
            self.array[i] = self.array[i + 1]
        self.length -= 1

    def print(self):
        print(self.array.tolist()[:self.length])
        
my_list = ArrayList(8)
my_list.print()

for i in range(10):
    my_list.append(i + 1)
my_list.print()

for i in range(10):
    my_list.prepend(i + 1)
my_list.print()

value = my_list.access(3)
print('my_list.access(3) = ' + str(value))

my_list.insert(8, 128)
my_list.print()

my_list.remove(4)
my_list.print()

my_list.set_head(10)
my_list.print()

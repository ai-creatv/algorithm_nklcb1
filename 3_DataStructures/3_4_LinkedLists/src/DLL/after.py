class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, self.head, None)
            self.head.prev = node
            self.head = node

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None, None)
            self.tail = self.head
        else:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node

    def set_head(self, index):
        if self.head is None:
            return False
        
        curr = self.head
        for _ in range(index):
            if curr.next is None:
                return False
            curr = curr.next
        
        self.head = curr
        self.head.prev = None
        return True

    def access(self, index):
        if self.head is None:
            return None
        
        curr = self.head
        for _ in range(index):
            if curr.next is None:
                return None
            curr = curr.next
        
        if curr is None:
            return None
        else:
            return curr.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False

        if index == 0:
            self.prepend(value)
            return True
        
        curr = self.head
        for _ in range(index):
            if curr.next is None:
                return False
            curr = curr.next
        
        if curr is None:
            node = Node(value, None, self.tail)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(value, curr, curr.prev)
            curr.prev.next = node
        return True

    def remove(self, index):
        if self.head is None:
            return False

        if index == 0:
            self.head = self.head.next
            if self.head is not None:
                self.head.prev = None
            return True
        
        curr = self.head
        for _ in range(index):
            if curr.next is None:
                return False
            curr = curr.next
        
        if curr is None:
            return False
        else:
            curr.prev.next = curr.next
            if curr.next is not None:
                curr.next.prev = curr.prev
            else:
                self.tail = curr.prev
            return True

    def print(self):
        if self.head is None:
            print('[]')
        else:
            curr = self.head
            print('[', end='')
            while curr.next is not None:
                print(curr.value, end=', ')
                curr = curr.next
            print(str(curr.value) + ']')


my_list = DoublyLinkedList()
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
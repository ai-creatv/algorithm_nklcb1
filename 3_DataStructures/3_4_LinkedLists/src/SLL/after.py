class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head is None

    def prepend(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            self.head = Node(value, self.head)

    def append(self, value):
        if self.head is None:
            self.head = Node(value, None)
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = Node(value, None)

    def set_head(self, index):
        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        self.head = curr
        return True

    def access(self, index):
        if self.head is None:
            return False

        curr = self.head
        for _ in range(index):
            if curr is None:
                return False
            curr = curr.next
        return curr.value

    def insert(self, index, value):
        if self.head is None and index > 0:
            return False
        
        if index == 0:
            self.prepend(value)
            return True
        
        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return False
            prev = curr
            curr = curr.next
        
        prev.next = Node(value, curr)
        return True

    def remove(self, index):
        if index == 0:
            if self.head is not None:
                self.head = self.head.next
                return True
            else:
                return False
        
        curr = self.head
        prev = None
        for _ in range(index):
            if curr is None:
                return False
            prev = curr
            curr = curr.next
        
        if curr is None:
            return False

        prev.next = curr.next
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
            

my_list = SinglyLinkedList()
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
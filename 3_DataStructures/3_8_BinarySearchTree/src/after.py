class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
       
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        # Ref: https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python/40885162
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __search(self, value):
        node = self.root
        parent = None
        direction = None

        while node:
            if node.value == value:
                break
            elif value < node.value:
                parent = node
                direction = 'left'
                node = node.left
            else:
                parent = node
                direction = 'right'
                node = node.right

        return parent, node, direction
    
    def insert(self, value):
        parent, node, direction = self.__search(value)

        if self.root is None:
            self.root = Node(value)
            return True
        
        if node is not None:
            return False

        if direction == 'left':
            parent.left = Node(value)
        else:
            parent.right = Node(value)

        return True
        

    def search(self, value):
        _, node, _ = self.__search(value)
        return node

    def remove(self, value):
        parent, node, direction = self.__search(value)

        if node is None:
            return False
        
        if (node.left is None) and (node.right is None):
            if parent is None:
                self.root = None
            elif direction == 'left':
                parent.left = None
            else:
                parent.right = None
        
        elif node.left is None:
            if parent is None:
                self.root = node.right
            elif direction == 'left':
                parent.left = node.right
            else:
                parent.right = node.right
        
        elif node.right is None:
            if parent is None:
                self.root = node.left
            elif direction == 'left':
                parent.left = node.left
            else:
                parent.right = node.left

        else:
            prev = node
            curr = node.left
            
            while curr.right:
                prev = curr
                curr = curr.right
            
            if prev != node:
                prev.right = curr.left
            else:
                prev.left = curr.left

            curr.left = node.left
            curr.right = node.right
            
            if parent is None:
                self.root = curr
            elif direction == 'left':
                parent.left = curr
            else:
                parent.right = curr

        return True


bst = BinarySearchTree()

import random
x = list(range(20))
random.shuffle(x)
for el in x:
    bst.insert(el)
bst.root.display()

bst.remove(6)
bst.root.display()

bst.remove(10)
bst.root.display()
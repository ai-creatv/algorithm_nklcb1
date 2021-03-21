import array

class BinaryTree:
    def __init__(self, arr):
        self.array = array.array('l', arr)    

    def preorder(self):
        def recursive(ind):
            nonlocal s
            s += str(self.array[ind]) + ' '

            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(self.array):
                recursive(left)
            if right < len(self.array):
                recursive(right)
        s = '['
        recursive(0)
        s += ']'
        print(s)

    def inorder(self):
        def recursive(ind):
            nonlocal s
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(self.array):
                recursive(left)

            s += str(self.array[ind]) + ' '

            if right < len(self.array):
                recursive(right)
        s = '['
        recursive(0)
        s += ']'
        print(s)

    def postorder(self):
        def recursive(ind):
            nonlocal s
            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(self.array):
                recursive(left)
            if right < len(self.array):
                recursive(right)
            s += str(self.array[ind]) + ' '
        s = '['
        recursive(0)
        s += ']'
        print(s)
    
    def bfs(self, value):
        for elem in self.array:
            if elem == value:
                return True
        return False

    def dfs(self, value):
        found = False
        def recursive(ind):
            nonlocal found
            if found is True:
                return
            
            if self.array[ind] == value:
                found = True
                return

            left = 2 * ind + 1
            right = 2 * ind + 2
            if left < len(self.array):
                recursive(left)
            if right < len(self.array):
                recursive(right)
        
        recursive(0)
        return found


tree = BinaryTree([i for i in range(13)])
tree.preorder()
tree.inorder()
tree.postorder()

print(tree.dfs(15))
print(tree.dfs(11))

print(tree.bfs(6))
print(tree.bfs(17))
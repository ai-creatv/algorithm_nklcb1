class MaxHeap:
    def __init__(self):
        self.arr = [None]
    
    def push(self, val):
        def need_swap(ind):
            parent = ind // 2
            if self.arr[ind] > self.arr[parent]:
                return True
            else:
                return False

        self.arr.append(val)
        curr = len(self.arr) - 1

        while curr > 1:
            if need_swap(curr):
                parent = curr // 2
                self.arr[curr], self.arr[parent] = self.arr[parent], self.arr[curr]
                curr = parent
            else:
                break


    def pop(self):
        def need_swap(ind, child):
            child
            if self.arr[child] > self.arr[ind]:
                return True
            else:
                return False

        if self.is_empty():
            return None

        val = self.arr[1]
        self.arr[1] = self.arr[-1]
        del self.arr[-1]
        curr = 1

        while curr < len(self.arr):
            left = curr * 2
            right = curr * 2 + 1

            if left < len(self.arr) and right < len(self.arr):
                if self.arr[left] > self.arr[right]:
                    if need_swap(curr, left):
                        self.arr[curr], self.arr[left] = self.arr[left], self.arr[curr]
                        curr = left
                    else:
                        break
                else:
                    if need_swap(curr, right):
                        self.arr[curr], self.arr[right] = self.arr[right], self.arr[curr]
                        curr = right
                    else:
                        break
            elif left < len(self.arr):
                if need_swap(curr, left):
                    self.arr[curr], self.arr[left] = self.arr[left], self.arr[curr]
                    curr = left
                else:
                    break
            elif right < len(self.arr):
                if need_swap(curr, right):
                    self.arr[curr], self.arr[right] = self.arr[right], self.arr[curr]
                    curr = right
                else:
                    break
            else:
                break
        
        return val


    def peek(self):
        return self.arr[1] if self.is_empty() else None

    def is_empty(self):
        return len(self.arr) == 1

heap = MaxHeap()

data = [1,6,32,14,60,2,5,66]
for elem in data:
    heap.push(elem)

while heap.is_empty() is False:
    print(heap.pop())
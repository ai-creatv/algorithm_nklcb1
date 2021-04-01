class HashTable:
    def __init__(self, hash_func=None, bucket_size=16):
        if hash_func is None:
            self.hash = hash
        else:
            self.hash = hash_func
        
        self.bucket_size = bucket_size
        self.bucket = [None]*bucket_size
    
    def set(self, key, value):
        index = self.hash(key) % self.bucket_size
        node = self.bucket[index]
        prev = None

        if node is None:
            self.bucket[index] = [key, value, None]
            return

        while node:
            if node[0] == key:
                node[1] = value
                return

            prev = node
            node = node[2]
            
        prev[2] = [key, value, None]

    def get(self, key):
        index = self.hash(key) % self.bucket_size
        node = self.bucket[index]

        while node:
            if node[0] == key:
                return node[1]
            
            node = node[2]

        return None

ht = HashTable(hash_func=lambda x: x % 20)
ht.set(0, 'a')
ht.set(20, 'b')
ht.set(40, 'c')

print(ht.get(0))
print(ht.get(20))
print(ht.get(40))
print(ht.get(60))

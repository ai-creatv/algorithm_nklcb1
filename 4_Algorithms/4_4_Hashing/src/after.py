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
            node = (key, value, None)

        while node:
            if node[0] == key:
                node[1] = value
                return

            if node[2]:
                prev = node
                node = node[2]
        
        prev[2] = (key, value, None)

    def get(self, key):
        index = self.hash(key) % self.bucket_size
        node = self.bucket[index]

        while node:
            if node[0] == key:
                return node[1]
            
            if node[2]:
                node = node[2]

        return None

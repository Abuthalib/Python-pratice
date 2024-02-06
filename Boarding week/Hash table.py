class hashTable:
    def __init__(self):
        self.max = 100
        self.arr = [None for i in range(self.max)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.max

    def __setitem__(self, key, value):
        h = self.get_hash(key)



c = hashTable()
print(c.get_hash("march 6"))

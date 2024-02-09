class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash_function(key)

        # Linear probing to find the next available slot
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Update the value if the key already exists
                self.values[index] = value
                return
            index = (index + 1) % self.size

        # Found an empty slot, insert the key-value pair
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash_function(key)

        # Linear probing to find the key or an empty slot
        while self.keys[index] is not None:
            if self.keys[index] == key:
                # Key found, return the corresponding value
                return self.values[index]
            index = (index + 1) % self.size

        # Key not found
        return None

# Example usage:
hash_table = HashTableLinearProbing(10)
hash_table.put("apple", 5)
hash_table.put("banana", 10)
hash_table.put("orange", 15)
hash_table.put("banana", 11)
hash_table.put("orange", 13)


print(hash_table.get("apple"))    # Output: 5
print(hash_table.get("banana"))   # Output: 10
print(hash_table.get("grape"))    # Output: None (Key not found)
print(hash_table.get("banana"))   # Output: 10
print(hash_table.get("orange")) 
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def display(self):
        print(self.items)


class stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Peeking from empty stack not allowed")

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


s = stack()
s.push(4)
s.push(3)
s.push(2)
s.push(1)
print("stack:",s.display())
q = Queue()
n = s.size()
for i in range(n):
    q.enqueue(s.pop())

for i in range(n):
    s.push(q.dequeue())

print("queue:",q.display())

print(("stack:",s.display()))

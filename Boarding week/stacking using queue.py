class Queue:
    def __init__(self):
        self.items =[]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self,data):
        self.items.append(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")
            return None
    
    def peek(self):
        if  not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None
    def display(self):
        return self.items


class stack:
    def __init__(self):
        self.items =[]

    def is_empty(self):
        return len(self.items) ==0
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
            
        else:
            raise IndexError("Pop ing from expty stack is not  allowed")
    
    def display(self):
        return self.items


s = stack()
q = Queue()
s.push(4)
s.push(2)
print("stack:",s.display())
n = len(s.items)
for i in range(n):
    q.enqueue(s.pop())
print("Queue from stack",q.display())

for i in range(n):
    s.push(q.dequeue())

print("stack from queue :",s.display())

for i in range(n):
    q.enqueue(s.pop())
print("Queue from stack",q.display())


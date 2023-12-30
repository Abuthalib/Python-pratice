import queue


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
            print("queue is empty")
            return None

    def front_element(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")
            return None

    def display(self):
        print("Queue elements :", self.items)


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.display()

print("front elemnt :",q.front_element())

dq = q.dequeue()
print("Dequeued :",dq)

q.display()
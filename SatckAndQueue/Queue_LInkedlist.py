class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        else:
            dequeued_data = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return  dequeued_data

    def front_element(self):
        if self.is_empty():
            print("queue is empty")
            return None
        else:
            return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data,end = "<-")
            current = current.next

q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.display()
print()
deq = q.dequeue()
print("Dequued :",deq)
q.display()
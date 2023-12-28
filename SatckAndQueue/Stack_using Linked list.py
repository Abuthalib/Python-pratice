class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            poped_data = self.top.data
            self.top = self.top.next
            return poped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data, end=" -->")
            current = current.next


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

print("Stack elements :")
stack.display()
print()
print("Peek", stack.peek())

popped_item = stack.pop()
print("Popped: ", popped_item)

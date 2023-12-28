class Stack:
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
            raise IndexError("Pop from an EMpty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Peek from an empty stack")

    def size(self):
        return len(self.items)

    def display(self):
        print(self.items)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.display()
stack.pop()
stack.display()
print(stack.peek())
print(stack.size())
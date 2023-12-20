class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtBegin(data)
        else:
            while current_node is not None and position + 1 != index:
                position = position + 1
                current_node = current_node.next
            if current_node is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index not present")

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")


LL = Linkedlist()

LL.insertAtBegin(0)
LL.insertAtBegin(1)
LL.insertAtBegin(2)
LL.insertAtBegin(3)
LL.insertAtBegin(4)
LL.display()

LL.insertAtIndex(99, 2)
LL.display()

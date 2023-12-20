class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
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

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")


LL = LinkedList()

LL.insertAtBegin(0)
LL.insertAtBegin(1)
LL.insertAtBegin(2)
LL.insertAtBegin(3)
LL.insertAtBegin(4)
LL.display()

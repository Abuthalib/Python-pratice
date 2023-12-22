# Create nodes
# create linked list
# Add nodes to list
# print linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtbegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        currentNode = self.head
        position = 0
        if position == index:
            self.insertAtbegin(data)
        else:
            while currentNode is not None and position != index:
                position = position + 1
                currentNode = currentNode.next
            if currentNode is not None:
                new_node.next = currentNode.next
                currentNode.next = new_node
            else:
                print("Index not present")

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("Finished")


# Node = data,next
LL = LinkedList()
LL.insertAtbegin("Hello")
LL.insertAtbegin("ABU")
LL.insertAtIndex("THALIB", 1)
LL.insertAtEnd("END")
LL.display()

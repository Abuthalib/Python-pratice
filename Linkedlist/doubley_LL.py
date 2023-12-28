class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DD_List:
    def __init__(self):
        self.head = None

    # insert at front of node
    def InsertAtFront(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # insert adter a give node
    def InsertAfter(self, prev_data, new_data):
        if not self.head:
            print("Doubly Linked List is empty")
            return
        current = self.head
        while current:
            if current.data == prev_data:
                new_node = Node(new_data)

                new_node.prev = current
                new_node.next = current.next

                if current.next:
                    current.next.prev = new_node

                current.next = new_node
                return
            current = current.next

    # insert before a given node
    def InsertBefore(self, next_data, data):
        if not self.head:
            print("Doubly linked List is empty")
            return
        current = self.head
        while current:
            if current.data == next_data:
                new_node = Node(data)

                new_node.next = current
                new_node.prev = current.prev

                if current.prev:
                    current.prev.next = new_node
                else:
                    self.head = new_node
                current.prev = new_node
                return
            current = current.next
        current = current.next

    def InsertAtEnd(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def deleteNode(self, data):
        if not self.head:
            print("doubly linked list is empty")
            return
        current = self.head

        if current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            return

        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def delete_from_start(self):
        if not self.head:
            print("Doubly LL is Empty")
            return
        self.head = self.head.next
        if self.head:
            self.head.prev = None

    def delete_from_end(self):
        if not self.head:
            print("Doubly LL is Empty")
            return
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        else:
            self.head = None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            current.prev = next_node
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


DL = DD_List()
DL.InsertAtFront(1)
DL.InsertAtFront(2)
DL.InsertAfter(1, 3)
DL.InsertBefore(2, 0)
DL.InsertAtEnd(4)
DL.InsertAtEnd(5)
DL.deleteNode(0)
DL.delete_from_start()
DL.delete_from_end()
DL.display()
DL.reverse()
DL.display()

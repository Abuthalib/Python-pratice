class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def display_list(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            while self.head is not None:
                print(self.head.data)
                self.head = self.head.next

    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self,data):
        new_node =  Node(data)
        if self.head is None:
            self.head = new_node
        else:
            while self.head.next is not None:
                self.head = self.head.next
            self.head.next = new_node

    def add_in_between(self,data,x):
        while self.head is not None:
            if x == self.head.data:
                break
            self.head = self.head.next

        if self.head is None:
            print("node is not present in  linked list")
        else:
            new_node = Node(data)
            new_node.next =self.head.next
            self.head.next = new_node




LL = LinkedList()
LL.display_list()

# adding at beginning
LL.add_begin(10)
LL.display_list()
LL.add_begin(11)
LL.display_list()


# adding at end
LL.add_end(12)
LL.display_list()


# adding in between
LL.add_in_between(11,10)
LL.display_list()


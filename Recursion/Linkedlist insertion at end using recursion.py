class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            self._append(self.head, data)

    def _append(self, node, data):
        if not node.next:
            node.next = Node(data)
        else:
            self._append(node.next, data)

    def _display(self,node):
        if not  node:
            print("None")
        else:
            print(node.data,end="-->")
            self._display(node.next)

    def display(self):
        self._display(self.head)


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)

ll.display()
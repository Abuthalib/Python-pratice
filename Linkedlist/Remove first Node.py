from singly_llist import LinkedList

L1 = LinkedList()


def remove_first(self):
    if self.head is None:
        return
    self.head = self.head.next


def remove_last(self):
    if self.head is None:
        return
    current = self.head
    while current.next.next:
        current = current.next
    current.next = None


def removeAtIndex(self, index):
    if self.head is None:
        return
    current = self.head
    position = 0
    if position == index:
        self.remove_first()
    else:
        while current is not None and position + 1 != index:
            position = position + 1
            current = current.next
        if current is not None:
            current.next = current.next.next
        else:
            print("Index not present")


#remove node og given data

def  remove_node(self,data):
    current = self.head
    if current.data == data:
        self.remove_first()
        return

    while current is not None and current.next.data != data:
        current = current.next

    if current is None:
        return
    else:
        current.next = current.next.next
















L1.insertAtbegin(6)
L1.insertAtbegin(5)
L1.insertAtbegin(4)
L1.insertAtbegin(3)
L1.insertAtbegin(2)
L1.insertAtbegin(1)
L1.display()

L1.remove_first = remove_first.__get__(L1)
L1.remove_last = remove_last.__get__(L1)
L1.removeAtIndex = removeAtIndex.__get__(L1)
L1.remove_node = remove_node.__get__(L1)

L1.remove_first()
L1.remove_last()
L1.removeAtIndex(3)
L1.remove_node(3)
L1.display()

from singly_llist import LinkedList

L2 = LinkedList()


def SizeOfLL(self):
    size = 0
    if self.head:
        current = self.head
        while current:
            size = size + 1
            current = current.next
        print("Length of LinkedList :", size)
    else:
        print("No List Found")


def Middle_LL(self):
    mid =0
    if self.head:
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            mid +=1
        print("Middle node :",mid)
    else:
        print("No List found")


L2.insertAtbegin(6)
L2.insertAtbegin(5)
L2.insertAtbegin(4)
L2.insertAtbegin(3)
L2.insertAtbegin(2)
L2.insertAtbegin(1)

L2.SizeOfLL = SizeOfLL.__get__(L2)
L2.Middle_LL = Middle_LL.__get__(L2)

L2.SizeOfLL()
L2.Middle_LL()
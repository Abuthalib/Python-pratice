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

    # remove prev Node
    def delete_node_and_prev(self, node_value):
        current_node = self.head
        prev_node = None

        # Handle the case where the node to be deleted is the head
        if current_node is not None and current_node.data == node_value:
            self.head = current_node.next
            return

        while current_node is not None and current_node.data != node_value:
            prev_node = current_node
            current_node = current_node.next

        if current_node is not None:
            if prev_node is not None:
                # Delete both the current_node and its previous node
                prev_node.next = current_node.next
            else:
                # If current_node is the first node, delete the first node
                self.head = current_node.next
        else:
            print(f"Node with value '{node_value}' not found.")



# Node = data,next
LL = LinkedList()
LL.insertAtbegin("Hello")
LL.insertAtbegin("ABU")
LL.insertAtIndex("THALIB", 1)
LL.insertAtEnd("END")
LL.display()
LL.delete_node_and_prev(jhu"THALIB")

print("\nAfter deletion:")
LL.display()

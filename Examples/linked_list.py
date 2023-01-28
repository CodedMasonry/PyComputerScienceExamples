
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def remove_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            current_node = None
            return
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return
        prev.next = current_node.next
        current_node = None

      
# Ex: Item = [1,"g", true]
def example():
    # Initialize the linked list
    llist = LinkedList()

    # Append some elements to the linked list
    llist.append("A")
    llist.append("B")
    llist.append("C")

    # Print the linked list
    print("Linked List:")
    llist.print_list()

    # Insert a new element at the beginning of the linked list
    llist.insert_at_beginning("X")

    # Print the modified linked list
    print("\nLinked List after inserting a new element at the beginning:")
    llist.print_list()

    # Remove an element from the linked list
    llist.remove_node("B")

    # Print the modified linked list
    print("\nLinked List after removing an element:")
    llist.print_list()
    print("\n")
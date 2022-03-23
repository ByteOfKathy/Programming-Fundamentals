"""
Implementation of Linked List Data Structure in python.
"""


# Classes

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    # Method to append (add at the end) node to the linked list.
    def append(self, value):
        new_node = Node(value)  # Take the value and create a new node.
        # If linked list doesn't have any node, add the first node as the head.
        if self.head is None:
            self.head = new_node
            self.tail = self.head  # Tail will be same as head since there is only one node.
            self.length += 1  # Increase the length.
            # return  # Only used when we were using the while loop traversal below.
        else:
            self.tail.next = new_node
            self.length += 1
        '''
        # The while loop below traverses the linked list to find the tail node and add a new node at the end.
        # The time complexity of this is O(n), therefore tail pointer is being used to track the last node so as to
        # make adding the new node O(1).
        current_node = self.head  # Set the current node to the head node.
        while True:
            if current_node.next is None:  # If current node pointer is None, i.e. the last node in the list is found.
                current_node.next = new_node  # Set the pointer of the last node to the new node.
                self.tail = current_node.next  # Set the tail as the pointer to the new node.
                self.length += 1  # Increment length by 1.
                break
            current_node = current_node.next  # Move to the next node in the list.
        '''

    # Method to add node at the beginning of the linked list.
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
            return
        current_node = self.head
        while True:
            if current_node.next is None:
                current_node.next = new_node
                self.tail = current_node.next
                self.length += 1
                break
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, "->",)
            current_node = current_node.next
        print("None")


# Declaration
linked = LinkedList()
linked.append(20)
linked.append(30)
linked.append(15)
linked.append(10)
linked.print_list()
print(linked.tail)

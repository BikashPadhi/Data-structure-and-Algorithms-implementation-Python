## Implementation of single linked list with all methods
## Author: Bikash Ranjan Padhi
import sys

class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    ## create linked_list
    def create_linkedlist(self, i):
        for var in range(i):
            j = int(input("enter value\n"))
            if self.head is None:
                self.head = node(j)
            else:
                last = self.head
                while(last.next):
                    last = last.next
                last.next = node(j)

    ## add a new node at the beginning
    def push_at_beginning(self, new_data):
        new_node = node(new_data)
        new_node.next = self.head
        self.head = new_node

    ## add node after a specific node
    def add_node_after_specfic_node(self, prev_node, new_node1):
        p_node = self.head
        prev_node1 = None
        while(p_node):
            if p_node.data == prev_node:
                prev_node1 = p_node
                break
            p_node = p_node.next
        if prev_node1 is None:
            print("node not found \n")
            return
        new_node = node(new_node1)
        new_node.next = prev_node1.next
        prev_node1.next = new_node

    ## reverse linkedlist
    def reverse_linkedlist(self):
        current = self.head
        prev_node = None
        while current is not None:
            next = current.next
            current.next = prev_node
            prev_node = current
            current = next
        self.head = prev_node

    ## print all nodes
    def print_list(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

    ## Insert a node at the end
    def insert_node_at_end(self, newdata):
        newnode = node(newdata)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current is not None:
                temp = current
                current = current.next
            temp.next = newnode

    ## delete node from linked list
    def delete_node_from_linkedlist(self, node):
        if self.head is None:
            print("linked list is empty \n")
            return
        current = self.head
        prev_node = None
        while(current):
            if current.data == node:
                break
            prev_node = current
            current = current.next
        if prev_node is None:
            self.head = current.next
        else:
            prev_node.next = current.next


Bikash_list = linkedlist()

Bikash_list.create_linkedlist(2)

Bikash_list.add_node_after_specfic_node(3, 5)

Bikash_list.push_at_beginning(5)

Bikash_list.print_list()

Bikash_list.reverse_linkedlist()

Bikash_list.insert_node_at_end(8)

Bikash_list.delete_node_from_linkedlist(8)

Bikash_list.print_list()

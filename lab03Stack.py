
import random
from datetime import time


class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class Stack:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def take(self):
        if self.head is None:
            print("stek is empty")
            return None
        temp = self.head
        if self.head.next is None:
            self.head = self.head.next
            return temp
        self.head = self.head.next
        return temp

    def printStack(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next


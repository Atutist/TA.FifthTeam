import random
from datetime import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def take(self):
        if self.head is None:
            print("arr is empty")
            return
        first = self.head
        self.head = self.head.next
        return first

    def printQueue(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next



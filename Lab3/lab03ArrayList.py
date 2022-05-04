import random
from datetime import time


class Node:
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class ArrayList:
    def __init__(self):
        self.head = None

    def length(self):
        if self.head is None:
            return 0
        counter = 1
        last = self.head
        while last.next:
            last = last.next
            counter += 1
        return counter

    def print(self):
        last = self.head
        while last.next:
            print(last.data)
            last = last.next
        print(last.data)

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def appendStart(self, data):
        new_node = Node(data)
        # new_node.next = self.head
        # self.head = new_node
        if self.head is None:
            print("There are no elements")
            return
        last = self.head
        self.head = new_node
        while last.next:
            last = last.next

    def appendCenter(self, data, pos):
        pos = round(pos)
        if self.head is None:
            print("arr is empty")
            return None
        if self.length() <= pos or pos <= 0:
            print("please enter correct position")
            return None
        new_node = Node(data)
        prev_node = self.head
        for i in range(pos - 1):
            prev_node = prev_node.next
        new_node.next = prev_node.next
        prev_node.next = new_node

    def pop(self):
        if self.head is None:
            print("arr is empty")
            return None
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

    def popPos(self, pos):
        if self.head is None:
            print("linked list is empty")
            return None
        pos = round(pos)
        if pos <= 0 or pos > self.length():
            print("please enter correct position")
            return None
        prev_node = self.head
        for i in range(pos - 1):
            prev_node = prev_node.next
        prev_node.next = prev_node.next.next

    def popStart(self):
        if self.head is None:
            print("arr is empty")
            return None
        self.head = self.head.next

    def searchByIndex(self, new_data):
        if self.head is None:
            print("There are no elements")
            return
        counter = 1
        last = self.head
        while last.next:
            if last.data == new_data:
                return counter
            last = last.next
            counter += 1

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next





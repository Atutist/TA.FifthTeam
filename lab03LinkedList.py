import random
from datetime import time


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
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

    def printRev(self):
        last = self.head
        while last.next:
            print(last.data)
            last = last.next
        print(last.data)
        while last.prev:
            print(last.data)
            last = last.prev
        print(last.data)

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def appendStart(self, data):
        new_node = Node(data)
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def appendCenter(self, data, pos):
        pos = round(pos)
        if self.head is None:
            print("arr is empty")
            return None
        if self.length() < pos or pos <= 0:
            print("please enter correct position")
            return None
        new_node = Node(data)
        prev_node = self.head
        for i in range(pos - 1):
            prev_node = prev_node.next
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.next.prev = new_node
        new_node.prev = prev_node

    def pop(self):
        if self.head is None:
            print("arr is empty")
            return None
        last = self.head
        while last.next.next:
            last = last.next
        last.next.prev = None
        last.next = None

    def popCenter(self, pos):
        if self.head is None:
            print("linked list is empty")
            return None
        pos = round(pos)
        if pos <= 0 or pos >= self.length():
            print("please enter correct position")
            return None
        prev_node = self.head
        for i in range(pos - 1):
            prev_node = prev_node.next
        prev_node.next = prev_node.next.next
        prev_node.next.prev = prev_node

    def popStart(self):
        if self.head is None:
            print("arr is empty")
            return None
        self.head.next.prev = None
        self.head = self.head.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next

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





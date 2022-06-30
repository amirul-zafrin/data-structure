from typing import Type
class Node:
    def __init__(self,data):
        self.data = data
        self.nxval = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def addFirst(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
        else:
            node.nxval = self.head
            self.head = node

        self.size += 1

    def addLast(self,data):
        node = Node(data)

        if self.head is None:
            self.head = node

        else:
            curr = self.head
            while curr.nxval is not None:
                curr = curr.nxval
            
            curr.nxval = node
        
        self.size += 1


    def addAtPos(self, data, position:int):
        if position > self.size + 1:
            raise Exception(f"Can't add value at position = {position}")

        idx = 1
        curr = self.head

        while position-1 != idx:
            curr = curr.nxval
            idx += 1

        node = Node(data)
        node.nxval = curr.nxval
        curr.nxval = node

        size += 1

    def removeFirst(self):
        if self.head is None:
            raise Exception(f"No value in the list")

        self.head = self.head.nxval
        self.size -= 1

    def removeLast(self):
        curr = self.head
        while curr.nxval.nxval is not None:
            curr = curr.nxval

        curr.nxval = None
        self.size -= 1

    def removeAt(self,position: int):
        if self.head is None:
            raise Exception(f"No value in the list")

        elif position > self.size:
            raise Exception(f"No value at position = {position}!")

        elif position == 1:
            return removeFirst()
        
        elif position == self.size:
            return removeLast()

        idx = 1
        curr = self.head

        while position-1 != idx:
            curr = curr.nxval
            idx += 1

        curr.nxval = curr.nxval.nxval
        self.size -= 1

    def traverse(self):
        curr = self.head
        lst = []
        while curr is not None:
            lst.append(curr.data)
            curr = curr.nxval
        print(lst)

    def reverse(self):
        prev = None
        curr = self.head

        while curr is not None:
            nxt = curr.nxval
            curr.nxval = prev
            prev = curr
            curr = nxt
        self.head = prev

    @classmethod
    def merge(self, list1, list2):
        newLL = LinkedList()
        if list1 is None:
            newLL = list2
        elif list2 is None:
            newLL = list1

        else:
            l1 = list1.head
            l2 = list2.head
            while l1 is not None and l2 is not None:
                newLL.addLast(l1.data)
                newLL.addLast(l2.data)
                l1 = l1.nxval
                l2 = l2.nxval
            
            while l1 is not None:
                newLL.addLast(l1.data)
                l1 = l1.nxval

            while l2 is not None:
                newLL.addLast(l2.data)
                l2 = l2.nxval
        return newLL
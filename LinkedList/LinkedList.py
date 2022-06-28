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

        if self.head == None:
            self.head = node
        else:
            node.nxval = self.head
            self.head = node

        self.size += 1

    def addLast(self,data):
        node = Node(data)

        if self.head == None:
            self.head = node

        else:
            curr = self.head
            while curr.nxval != None:
                curr = curr.nxval
            
            curr.nxval = node
        
        self.size += 1

    def addAtPos(self, data, position:int):
        if position > self.size:
            raise Exception(f"No value at position = {position}!")

        elif position == 1:
            return addFirst(data)
        
        elif position == self.size:
            return addLast(data)

        idx = 1
        curr = self.head

        while(position-1 != idx):
            curr = curr.nxval
            idx += 1

        node = Node(data)
        node.nxval = curr.nxval
        curr.nxval = node

    def removeFirst(self):
        self.head = self.head.nxval

    def removeLast(self):
        curr = self.head
        while(curr.nxval.nxval != None):
            curr = curr.nxval

        curr.nxval = None

    def removeAt(self,position: int):
        if position > self.size:
            raise Exception(f"No value at position = {position}!")

        elif position == 1:
            return removeFirst()
        
        elif position == self.size:
            return removeLast()

        idx = 1
        curr = self.head

        while(position-1 != idx):
            curr = curr.nxval
            idx += 1

        curr.nxval = curr.nxval.nxval

    def traverse(self):
        curr = self.head
        lst = []
        while(curr != None):
            lst.append(curr.data)
            curr = curr.nxval
        print(lst)

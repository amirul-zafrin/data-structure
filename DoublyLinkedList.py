from LinkedList import Node

class DNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prval = None
    
    def __str__(self):
        return f"{self.data}"

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addHead(self,data):
        node = DNode(data)

        if self.head == None:
            self.head = node
            self.tail = self.head
            self.size += 1
        else:
            self.head.prval = node
            node.nxval = self.head
            self.head = node
            self.size += 1

    def addTail(self,data):
        node = DNode(data)

        if self.head == None:
            raise Exception("No head to add tail!")

        else:
            self.tail.nxval = node
            node.prval = self.tail
            self.tail = node
            self.size += 1

    def addAt(self,data,position: int):
        idx = 1
        node = DNode(data)
        if position > self.size:
            raise Exception(f"Cannot add value outside of the list")
        elif(self.size / 2 >= position):
            curr = self.head
            while(idx != position):
                curr = curr.nxval
                idx += 1

            node.prval = curr.prval
            node.nxval = curr
            node.prval.nxval = node
            node.nxval.prval = node
            self.size += 1
        else:
            curr = self.tail
            while(idx-1 != self.size - position):
                curr = curr.prval
                idx += 1
            node.prval = curr.prval
            node.nxval = curr
            node.prval.nxval = node
            node.nxval.prval = node
            self.size += 1

    def removeHead(self):
        self.head = self.head.nxval
        self.head.prval = None
        self.size -= 1


    def removeTail(self):
        self.tail = self.tail.prval
        self.tail.nxval = None
        self.size -= 1

    def removeAt(self,position: int):
        idx = 1
        if position > self.size:
            raise Exception(f"Value at position = {position} is not exist!")
        elif(self.size / 2 >= position):
            curr = self.head
            while(idx != position):
                curr = curr.nxval
                idx += 1
            temp = curr
            curr.prval.nxval = temp.nxval
            curr.nxval.prval = temp.prval
            self.size -= 1
        else:
            curr = self.tail
            while(idx-1 != self.size - position):
                curr = curr.prval
                idx += 1
            temp = curr
            curr.prval.nxval = temp.nxval
            curr.nxval.prval = temp.prval
            self.size -= 1

    def travForward(self):
        if self.head == None:
            raise Exception("List is empty")
        
        curr = self.head
        lst = []

        while curr.nxval is not None:
            lst.append(curr.data)
            curr = curr.nxval

        lst.append(self.tail.data)
        print(f"List: {lst}")

    def travBackward(self):
        if self.head == None:
            raise Exception("List is empty")
        
        curr = self.tail
        lst = []

        while curr.prval is not None:
            lst.append(curr.data)
            curr = curr.prval
     
        lst.append(self.head.data)
        print(f"List: {lst}")

    def reverse(self):
        curr = self.head
        while curr is not None:
            curr.nxval, curr.prval = curr.prval, curr.nxval
            curr = curr.prval

        self.head, self.tail = self.tail, self.head
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

# TODO insert at beginning
    def addFirst(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        else:
            node.nxval = self.head
            self.head = node

        self.size += 1

# TODO insert at the end
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

# TODO insert at any position
    def addAtPos(self, data, position):
        if position > self.size:
            raise Exception(f"No value at position = {position}!")

        elif position == 1:
            return addFirst(data)
        
        elif position == self.size:
            return addLast(data)

        idx = 1
        curr = self.head.nxval

        while(position - 1  != idx):
            curr = curr.nxval
            idx += 1

        node = Node(data)
        node.nxval = curr.nxval
        curr.nxval = node

# TODO Remove end

# TODO Remove tail

# TODO Remove any pos 

# TODO traverse
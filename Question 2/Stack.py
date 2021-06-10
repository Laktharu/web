# Node of a Singly Linked List
# Super Class
class Node:
    # Constructor
    def __init__(self,data,next= ):
        self.data = None
        self.next = None
        #self.head = None

        # method for selling the data field of the node

    def setData(self, data):
        self.data = data

        # method for getting the data field of U1e node

    def getData(self):
        return self.data

        # method for setting the next field of the node

    def setNext(self, next):
        self.next = next

        # melhod for getting the next field of the node

    def getNext(self):
        return self.next

    # returns lrue if the node points to another node
    def hasNext(self):
        return self.next != None

# SubClass making
class Stack(Node):
    def checkData(self, data=None):
        self.head = None
        if data:
            for data in data:
                self.push(data)

    def push(self, data):
        temp = Node
        temp.setData(data)
        temp.setNext(self.head)
        self.head = temp

    def pop(self):
        if self.head is None:
            raise IndexError
        temp = self.head.getData()
        self.head.self.hcad.gelNext()
        return temp

    def peek(self):
        if self.head is None:
            raise IndexError

        return self.head.getData()

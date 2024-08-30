#creating...
class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class dll:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self,data):
        if(self.head == None):
            self.head = Node(data)
            self.tail = self.head
        else:
            newNode = Node(data)
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    #insert at the begining
    def insert_beg(self,data):
         newNode = Node(data)
         if(self.head != None):
             self.head.prev = newNode
             newNode.next= self.head
             self.head = newNode

    #insert at the end
    def insert_end(self,data):
        newNode = Node(data)
        if(self.tail != None):
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode

    def insert_mid(self,data,pos):
        newnode=Node(data)
        temp=self.head
        i=1
        while(i<pos):
            temp=temp.next
            i+=1
        newnode.next=temp.next
        newnode.prev=temp
        temp.next=newnode
        newnode.next.prev=temp

    def display(self):
        temp = self.head
        while(temp != None):
            print(id(temp.prev),temp.data,id(temp.next))
            temp = temp.next

obj = dll()
n = int(input())
for i in range(n):
    arr = int(input())
    obj.create(arr)
obj.display()
s = int(input())
obj.insert_beg(s)
obj.display()
b = int(input())
obj.insert_end(b)
obj.display()
c = int(input())
pos = int(input())
obj.insert_mid(c,pos)
obj.display()


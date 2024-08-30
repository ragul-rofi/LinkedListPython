class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sll():
    def __init__(self):
        self.head = None

    def create(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    #inseriton at the begining

    def ins_beg(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # inseriton at the end

    def ins_end(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode

    #insertion at a position

    def ins_pos(self,data,pos):
        newNode = Node(data)
        if pos == 0:
            newNode.next = self.head
            self.head = newNode
        temp = self.head
        i = 0
        while temp is not None and i<pos -1:
            temp = temp.next
            i += 1
        if temp is None:
            print("Position is out of bounds")
            return
        newNode.next = temp.next
        temp.next = newNode

    def display(self):
        temp = self.head
        while(temp != None):
            print(temp.data)
            temp= temp.next

obj = sll()
n = int(input("Enter nuber of initial elements : "))
for i in range(n):
    arr = int(input("Enter element : "))
    obj.create(arr)
print()
obj.display()
print()
s = int(input("Enter the element that inserts at the begining : "))
obj.ins_beg(s)
print("Current Array : ")
obj.display()
print()

a = int(input("Enter the element that inserts at the end : "))
obj.ins_end(a)
print("Current Array : ")
obj.display()
print()

b = int(input("Enter the element that inserts at the middle : "))
pos = int(input("Enter the position : "))
print("Current Array : ")
obj.ins_pos(b,pos)
obj.display()



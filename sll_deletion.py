class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll_del:
    def __init__(self):
        self.head = None
        self.tail = None

    def create(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail=self.head
        else:
            self.tail.next=newNode
            self.tail=newNode


    def del_beg(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp

    def del_pos(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.del_beg()
            return

        temp = self.head

        for _ in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of bounds")
                return
            temp = temp.next

        if temp.next == self.tail:
            self.del_end()
        else:
            temp.next = temp.next.next

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next
        print("None")

obj = sll_del()
n = int(input("Enter nuber of initial elements : "))
for i in range(n):
    arr = int(input("Enter element : "))
    obj.create(arr)
print()
obj.display()
print()

obj.del_beg()
print("Current Array : ")
obj.display()
print()


obj.del_end()
print("Current Array : ")
obj.display()
print()

pos = int(input("Enter the position : "))
print("Current Array : ")
obj.del_pos(pos)
obj.display()



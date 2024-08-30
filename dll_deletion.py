class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class dll_del:
    def __init__(self):
        self.head = None
        self.tail = None

    def del_beg(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def del_end(self):
        if self.tail is None:
            print("List is empty")
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def del_pos(self, position):
        if self.head is None:
            print("List is empty")
            return

        if position == 0:
            self.del_beg()
            return

        current = self.head

        for _ in range(position):
            if current is None:
                print("Position out of bounds")
                return
            current = current.next

        if current == self.tail:
            self.del_end()
        else:
            current.prev.next = current.next
            current.next.prev = current.prev

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

obj = dll_del()
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


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None  # Added prev pointer
        self.next = None

class cdll:
    def __init__(self):
        self.head = None
        self.tail = None  # Added tail pointer

    def create(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode  # Updated tail pointer
            self.head.prev = self.tail  # Made it circular
            self.tail.next = self.head  # Made it circular
        else:
            self.tail.next = newNode
            newNode.prev = self.tail  # Maintained circular link
            self.tail = newNode
            self.tail.next = self.head  # Maintained circular link
            self.head.prev = self.tail  # Maintained circular link

    def ins_beg(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode  # Updated tail pointer
            self.head.prev = self.tail  # Made it circular
            self.tail.next = self.head  # Made it circular
        else:
            newNode.next = self.head
            self.head.prev = newNode  # Maintained circular link
            self.head = newNode
            self.head.prev = self.tail  # Maintained circular link
            self.tail.next = self.head  # Maintained circular link

    def ins_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            self.tail = newNode  # Updated tail pointer
            self.head.prev = self.tail  # Made it circular
            self.tail.next = self.head  # Made it circular
        else:
            self.tail.next = newNode
            newNode.prev = self.tail  # Maintained circular link
            self.tail = newNode
            self.tail.next = self.head  # Maintained circular link
            self.head.prev = self.tail  # Maintained circular link

    def ins_pos(self, data, pos):
        newNode = Node(data)
        if pos == 0:
            self.ins_beg(data)
            return
        temp = self.head
        i = 0
        while temp is not None and i < pos - 1:
            temp = temp.next
            i += 1
        if temp is None:
            print("Position is out of bounds")
            return
        newNode.next = temp.next
        if temp.next == self.head:  # If inserted at the end, update tail
            self.tail = newNode
        else:
            temp.next.prev = newNode  # Maintained circular link
        temp.next = newNode
        newNode.prev = temp  # Maintained circular link

    def display(self):
        if self.head is None:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" <-> ")
            temp = temp.next
            if temp == self.head:  # Stop if we loop back to the head
                break
        print("(head)")

# Example usage
obj = cdll()
n = int(input("Enter number of initial elements: "))
for i in range(n):
    arr = int(input("Enter element: "))
    obj.create(arr)
print()
obj.display()
print()

s = int(input("Enter the element to insert at the beginning: "))
obj.ins_beg(s)
print("Current List: ")
obj.display()
print()

a = int(input("Enter the element to insert at the end: "))
obj.ins_end(a)
print("Current List: ")
obj.display()
print()

b = int(input("Enter the element to insert in the middle: "))
pos = int(input("Enter the position: "))
print("Current List: ")
obj.ins_pos(b, pos)
obj.display()
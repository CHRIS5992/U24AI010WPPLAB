class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print('None')

    def add(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def remove(self, value):
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        if not temp:
            return
        prev.next = temp.next

lst = LinkedList()
lst.add(3)
lst.add(7)
lst.add(2)
lst.add(9)
lst.show()
lst.remove(7)
lst.show()
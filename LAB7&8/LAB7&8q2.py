class Queue:
    def __init__(self):
        self.items = []

    def insert(self, val):
        self.items.append(val)

    def delete(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def display(self):
        print(self.items)

q = Queue()
q.insert(5)
q.insert(10)
q.insert(15)
q.display()
q.delete()
q.display()

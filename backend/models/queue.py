class Queue:
    def __init__(self):
        self.items = []
        # FIFO

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty() is True:
            return None
        temp = self.items[0]
        del self.items[0]
        return temp

    def peek(self):
        if self.is_empty() is True:
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

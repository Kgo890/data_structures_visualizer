class Stack:
    def __init__(self):
        self.items = []
        # FILO

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty() is True:
            return None
        temp = self.items[-1]
        del self.items[-1]
        return temp

    def peek(self):
        if self.is_empty() is True:
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def reset(self):
        self.items.clear()

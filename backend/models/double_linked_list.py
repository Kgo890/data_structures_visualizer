class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, item):
        new_node = DoubleNode(item)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        if self.tail is None:
            self.tail = new_node

    def insert_at_tail(self, item):
        new_node = DoubleNode(item)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_from_front(self):
        if self.head is None:
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def delete_from_back(self):
        if self.tail is None:
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def search(self, item):
        current = self.head
        index = 0
        while current is not None:
            if current.value == item:
                return index
            else:
                current = current.next
                index += 1
        return -1

    def traverse(self):
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return values

    def reverse_traverse(self):
        values = []
        current = self.tail
        while current is not None:
            values.append(current.value)
            current = current.prev
        return values

    def reset(self):
        self.head = None
        self.tail = None

    def reverse(self):
        current = self.head
        prev_node = None
        while current is not None:
            next_node = current.next
            current.next = prev_node
            current.prev = next_node
            prev_node = current
            current = next_node
        self.head, self.tail = self.tail, self.head

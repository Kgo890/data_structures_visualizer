class SingleNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, item):
        new_node = SingleNode(item)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current is not None:
            current = current.next
        current.next = new_node

    def delete(self, item):
        current = self.head
        prev = None

        while current is not None:
            if current.value == item:
                if prev is not None:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, item):
        current = self.head
        while current is not None:
            if current.value == item:
                return True
            else:
                current = current.next
        return False

    def traverse(self):
        current = self.head
        while current is not None:
            print(current.value, end='->')
            current = current.next
        print('None')


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

    def delete(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            current = current.next
        return False

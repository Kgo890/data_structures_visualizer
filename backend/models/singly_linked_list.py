class SingleNode:
    def __init__(self, value):
        self.value = value
        self.next = None


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
        while current.next is not None:
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

    def reset(self):
        self.head = None

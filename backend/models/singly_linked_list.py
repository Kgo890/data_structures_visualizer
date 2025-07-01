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

    def delete_from_front(self):
        if self.head is None:
            return None
        value = self.head.value
        self.head = self.head.next
        return value

    def delete_from_back(self):
        if self.head is None:
            return None
        if self.head.next is None:
            value = self.head.value
            self.head = None
            return value

        current = self.head
        while current.next.next:
            current = current.next

        value = current.next.value
        current.next = None
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

    def reverse(self):
        prev = None
        current = self.head
        steps = []

        while current is not None:
            next_node = current.next
            steps.append({
                'current': current.value,
                'next': next_node.value if next_node else None,
                'prev': prev.value if prev else None
            })
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        return steps

    def reset(self):
        self.head = None

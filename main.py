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


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return
        else:
            current = self.root
            while current is not None:
                if new_node.value < current.value:
                    if current.left is None:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self):
        pass

    def in_order_traverse(self):
        nums = []

        def helper(tree_node, nums):
            if tree_node is None:
                return

            helper(tree_node.left, nums)
            nums.append(tree_node.value)
            helper(tree_node.right, nums)

        helper(self.root, nums)
        return nums

    def pre_order_traverse(self):
        nums = []

        def helper(tree_node, nums):
            if tree_node is None:
                return
            nums.append(tree_node.value)
            helper(tree_node.left, nums)
            helper(tree_node.right, nums)

        helper(self.root, nums)
        return nums

    def post_order_traverse(self):
        nums = []

        def helper(tree_node, nums):
            if tree_node is None:
                return
            helper(tree_node.left, nums)
            helper(tree_node.right, nums)
            nums.append(tree_node.value)

        helper(self.root, nums)
        return nums

    def height(self):
        pass

    def delete(self):
        pass


def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def selection_sort(nums):
    n = len(nums)
    for i in range(0, n - 1):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        current_index = i
        while current_index > 0 and nums[current_index - 1] > nums[current_index]:
            nums[current_index], nums[current_index - 1] = nums[current_index - 1], nums[current_index]
            current_index -= 1
    return nums


def merge_sort(nums):
    if len(nums) < 2:
        return nums

    left = nums[:len(nums) // 2]
    right = nums[len(nums) // 2:]
    left_side = merge_sort(left)
    right_side = merge_sort(right)
    final = []
    i = j = 0
    while i < len(left_side) and j < len(right_side):
        if left_side[i] <= right_side[j]:
            final.append(left_side[i])
            i += 1
        else:
            final.append(right_side[j])
            j += 1
    final.extend(left_side[i:])
    final.extend(right_side[j:])
    return final


def quick_sort(nums, low, high):
    if low < high:
        middle = partition(nums, low, high)
        quick_sort(nums, low, middle - 1)
        quick_sort(nums, middle + 1, high)
    return nums


def partition(nums, low, high):
    pivot = nums[high]
    i = low - 1
    for j in range(low, high):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[high] = nums[high], nums[i + 1]
    return i + 1


nums = [5, 3, 8, 2, 6]

#print(selection_sort(nums))
#print(insertion_sort(nums))
#print(merge_sort(nums))


print(quick_sort(nums, 0, len(nums) - 1))

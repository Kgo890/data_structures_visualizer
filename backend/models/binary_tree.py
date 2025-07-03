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

    def search(self, value):
        return self._search(self.root, value, 0)

    def _search(self, node, value, depth):
        if node is None:
            return -1
        if node.value == value:
            return depth
        elif value < node.value:
            return self._search(node.left, value, depth + 1)
        else:
            return self._search(node.right, value, depth + 1)

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
        current = self.root
        if current is None:
            return 0

        def helper(tree_node):
            if tree_node is None:
                return 0
            left_height = helper(tree_node.left)
            right_height = helper(tree_node.right)

            return 1 + max(left_height, right_height)

        return helper(current)

    def delete(self, value):
        parent = self.root
        current = self.root
        while current is not None:
            if current.value == value:

                # leaf node deletion
                if current.left is None and current.right is None:
                    if current == self.root:
                        self.root = None
                        break

                    if parent.left == current:
                        parent.left = None
                        break

                    if parent.right == current:
                        parent.right = None
                        break

                # one child cases (right or left)
                elif current.left is None:
                    if current == self.root:
                        self.root = current.right
                        break
                    else:
                        if current == parent.left:
                            parent.left = current.right
                            break
                        elif current == parent.right:
                            parent.right = current.right
                            break

                elif current.right is None:
                    if current == self.root:
                        self.root = current.left
                        break
                    else:
                        if current == parent.left:
                            parent.left = current.left
                            break
                        elif current == parent.right:
                            parent.right = current.left
                            break
                # two children
                elif current.left is not None and current.right is not None:
                    successor_parent = current
                    successor = current.right

                    while successor.left is not None:
                        successor_parent = successor
                        successor = successor.left
                    current.value = successor.value
                    if successor_parent.left == successor:
                        successor_parent.left = successor.right
                    else:
                        successor_parent.right = successor.right

            elif value < current.value:
                parent = current
                current = current.left
            else:
                parent = current
                current = current.right

    def reset(self):
        self.root = None

    def serialize(self):
        def node_to_dict(node):
            if node is None:
                return None
            return {
                "value": node.value,
                "left": node_to_dict(node.left),
                "right": node_to_dict(node.right)
            }
        return node_to_dict(self.root)

    def count_leaf_nodes(self):
        def count(node):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return 1
            return count(node.left) + count(node.right)

        return count(self.root)

    def is_balanced(self):
        def check(node):
            if node is None:
                return 0, True
            left_height, left_balanced = check(node.left)
            right_height, right_balanced = check(node.right)
            height = 1 + max(left_height, right_height)
            balanced = (
                    abs(left_height - right_height) <= 1
                    and left_balanced
                    and right_balanced
            )
            return height, balanced

        _, balanced = check(self.root)
        return balanced



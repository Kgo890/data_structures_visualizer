class RBNode:
    def __init__(self, val):
        self.red = False
        self.parent = None
        self.val = val
        self.left = None
        self.right = None


class RBTree:
    def __init__(self):
        self.nil = RBNode(None)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil

    def insert(self, val):
        new_node = RBNode(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                # duplicate, just ignore
                return

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, current):
        while current != self.root and current.parent.red:
            parent = current.parent
            grandparent = parent.parent
            if grandparent is None:
                break

            if parent == grandparent.left:
                uncle = grandparent.right
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                else:
                    if current == parent.right:
                        current = parent
                        self.rotate_left(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_right(grandparent)
            else:
                uncle = grandparent.left
                if uncle.red:
                    uncle.red = False
                    parent.red = False
                    grandparent.red = True
                    current = grandparent
                else:
                    if current == parent.left:
                        current = parent
                        self.rotate_right(current)
                        parent = current.parent
                    parent.red = False
                    grandparent.red = True
                    self.rotate_left(grandparent)

        self.root.red = False

    def exists(self, val):
        curr = self.root
        while curr != self.nil and val != curr.val:
            if val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return curr

    def rotate_left(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.right == self.nil:
            return
        pivot = pivot_parent.right
        pivot_parent.right = pivot.left
        if pivot.left != self.nil:
            pivot.left.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.left:
            pivot_parent.parent.left = pivot
        else:
            pivot_parent.parent.right = pivot
        pivot.left = pivot_parent
        pivot_parent.parent = pivot

    def rotate_right(self, pivot_parent):
        if pivot_parent == self.nil or pivot_parent.left == self.nil:
            return
        pivot = pivot_parent.left
        pivot_parent.left = pivot.right
        if pivot.right != self.nil:
            pivot.right.parent = pivot_parent

        pivot.parent = pivot_parent.parent
        if pivot_parent.parent is None:
            self.root = pivot
        elif pivot_parent == pivot_parent.parent.right:
            pivot_parent.parent.right = pivot
        else:
            pivot_parent.parent.left = pivot
        pivot.right = pivot_parent
        pivot_parent.parent = pivot

    def search(self, value):
        current = self.root
        while current != self.nil:
            if value == current.val:
                return current.val
            elif value < current.val:
                current = current.left
            else:
                current = current.right
        return None

    def delete(self, value):
        z = self.root
        while z != self.nil:
            if z.val == value:
                break
            elif value < z.val:
                z = z.left
            else:
                z = z.right
        if z == self.nil:
            return  # Value not found

        y = z
        y_original_red = y.red
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_red = y.red
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.red = z.red

        if not y_original_red:
            self.fix_delete(x)

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def fix_delete(self, x):
        while x != self.root and not x.red:
            if x == x.parent.left:
                w = x.parent.right
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if not w.left.red and not w.right.red:
                    w.red = True
                    x = x.parent
                else:
                    if not w.right.red:
                        w.left.red = False
                        w.red = True
                        self.rotate_right(w)
                        w = x.parent.right
                    w.red = x.parent.red
                    x.parent.red = False
                    w.right.red = False
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.red:
                    w.red = False
                    x.parent.red = True
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if not w.left.red and not w.right.red:
                    w.red = True
                    x = x.parent
                else:
                    if not w.left.red:
                        w.right.red = False
                        w.red = True
                        self.rotate_left(w)
                        w = x.parent.left
                    w.red = x.parent.red
                    x.parent.red = False
                    w.left.red = False
                    self.rotate_right(x.parent)
                    x = self.root
        x.red = False

    def reset(self):
        self.root = self.nil

    def count_leaf_nodes(self):
        def helper(node):
            if node == self.nil:
                return 0
            if node.left == self.nil and node.right == self.nil:
                return 1
            return helper(node.left) + helper(node.right)

        return helper(self.root)

    def in_order_traverse(self):
        result = []

        def helper(node):
            if node == self.nil:
                return
            helper(node.left)
            result.append(node.val)
            helper(node.right)

        helper(self.root)
        return result

    def pre_order_traverse(self):
        result = []

        def helper(node):
            if node == self.nil:
                return
            result.append(node.val)
            helper(node.left)
            helper(node.right)

        helper(self.root)
        return result

    def post_order_traverse(self):
        results = []

        def helper(node):
            if node == self.nil:
                return
            helper(node.left)
            helper(node.right)
            results.append(node.val)

        helper(self.root)
        return results

    def height(self):
        def helper(tree_node):
            if tree_node == self.nil:
                return 0
            return 1 + max(helper(tree_node.left), helper(tree_node.right))

        return helper(self.root)

    def serialize(self):
        def node_to_dict(node):
            if node == self.nil:
                return None
            return {
                "value": node.val,
                "color": "red" if node.red else "black",
                "left": node_to_dict(node.left),
                "right": node_to_dict(node.right)
            }
        return node_to_dict(self.root)


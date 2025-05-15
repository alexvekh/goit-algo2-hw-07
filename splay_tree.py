class Node:
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class SplayCache:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        """Вставляє (key, value) у splay-дерево."""
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert_node(self.root, key, value)

    def _insert_node(self, current, key, value):
        if key < current.key:
            if current.left:
                self._insert_node(current.left, key, value)
            else:
                current.left = Node(key, value, parent=current)
                self._splay(current.left)
        elif key > current.key:
            if current.right:
                self._insert_node(current.right, key, value)
            else:
                current.right = Node(key, value, parent=current)
                self._splay(current.right)
        else:
            current.value = value
            self._splay(current)

    def find(self, key):
        node = self.root
        while node:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                self._splay(node)
                return node.value
        return -1

    def _splay(self, node):
        while node.parent:
            if node.parent.parent is None:
                if node == node.parent.left:
                    self._rotate_right(node.parent)
                else:
                    self._rotate_left(node.parent)
            elif node == node.parent.left and node.parent == node.parent.parent.left:
                self._rotate_right(node.parent.parent)
                self._rotate_right(node.parent)
            elif node == node.parent.right and node.parent == node.parent.parent.right:
                self._rotate_left(node.parent.parent)
                self._rotate_left(node.parent)
            else:
                if node == node.parent.left:
                    self._rotate_right(node.parent)
                    self._rotate_left(node.parent)
                else:
                    self._rotate_left(node.parent)
                    self._rotate_right(node.parent)

    def _rotate_right(self, node):
        left = node.left
        if not left:
            return
        node.left = left.right
        if left.right:
            left.right.parent = node
        left.parent = node.parent
        if not node.parent:
            self.root = left
        elif node == node.parent.left:
            node.parent.left = left
        else:
            node.parent.right = left
        left.right = node
        node.parent = left

    def _rotate_left(self, node):
        right = node.right
        if not right:
            return
        node.right = right.left
        if right.left:
            right.left.parent = node
        right.parent = node.parent
        if not node.parent:
            self.root = right
        elif node == node.parent.left:
            node.parent.left = right
        else:
            node.parent.right = right
        right.left = node
        node.parent = right

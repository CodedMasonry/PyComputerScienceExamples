class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        current = self.root
        while True:
            if data < current.data:
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

    def search(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, data):
      self.root, deleted = self._delete(self.root, data)
      return deleted

    def _delete(self, node, data):
        if node is None:
            return node, False
    
        deleted = False
        if data == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif data < node.data:
            node.left, deleted = self._delete(node.left, data)
        else:
            node.right, deleted = self._delete(node.right, data)
        return node, deleted


    def find_min(self):
        current = self.root
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def pre_order_traversal(self):
        self._pre_order_traversal(self.root)

    def _pre_order_traversal(self, node):
        if node is not None:
            print(node.data)
            self._pre_order_traversal(node.left)
            self._pre_order_traversal(node.right)

    def in_order_traversal(self):
        self._in_order_traversal(self.root)

    def _in_order_traversal(self, node):
        if node is not None:
            self._in_order_traversal(node.left)
            print(node)

def example():
    print("Binary Search Tree:")
    bst = BinarySearchTree()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(1)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)

    print("In-order traversal:")
    bst.in_order_traversal()
    print("\nPre-order traversal:")
    bst.pre_order_traversal()

    print("\nSearching for 5:")
    print(bst.search(5))

    print("\nSearching for 10:")
    print(bst.search(10))

    print("\nMinimum value:")
    print(bst.find_min().data)

    print("\nMaximum value:")
    print(bst.find_max().data)

    bst.delete(5)

    print("\nIn-order traversal after deleting 5:")
    bst.in_order_traversal()

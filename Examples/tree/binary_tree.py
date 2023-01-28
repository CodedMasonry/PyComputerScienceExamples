class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
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

def print_tree(node, prefix="", is_left=True):
    if not node:
        print("Empty Tree")
        return
    if node.right:
        print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
    print(prefix + ("└── " if is_left else "┌── ") + str(node.data))
    if node.left:
        print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

def example():
  tree = BinaryTree()
  tree.insert(5)
  tree.insert(3)
  tree.insert(7)
  tree.insert(2)
  tree.insert(4)
  tree.insert(6)
  tree.insert(8)
  print("\n Binary Tree:")
  print_tree(tree.root)
  print("\n")
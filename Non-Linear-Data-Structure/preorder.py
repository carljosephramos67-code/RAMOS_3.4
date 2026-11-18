class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


root = Node("C")
root.left = Node("A")
root.right = Node("R")

root.left.left = Node("L")
root.left.right = Node("R")

root.right.left = Node("A")
root.right.right = Node("M")

root.left.left.left = Node("O")
root.left.left.right = Node("S")

print("Preorder Traversal:")
preorder(root)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


root = Node("C")
root.left = Node("A")
root.right = Node("R")

root.left.left = Node("L")
root.left.right = Node("R")

root.right.left = Node("A")
root.right.right = Node("M")

root.left.left.left = Node("O")
root.left.left.right = Node("S")

print("Inorder Traversal:")
inorder(root)
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


root = Node("C")
root.left = Node("A")
root.right = Node("R")

root.left.left = Node("L")
root.left.right = Node("R")

root.right.left = Node("A")
root.right.right = Node("M")

root.left.left.left = Node("O")
root.left.left.right = Node("S")

print("Postorder Traversal:")
postorder(root)
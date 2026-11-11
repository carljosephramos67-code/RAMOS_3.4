r"""
Binary Tree structure (Assessment 3.3) - RAMOS

           R (1)
         /       \
      A (2)     M (3)
      /   \
   O (4)  S (5)
"""
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def build(self):
        """Build the tree from the diagram."""
        self.root = Node("R")
        self.root.left = Node("A")
        self.root.right = Node("M")
        self.root.left.left = Node("O")
        self.root.left.right = Node("S")

    def bfs(self):
        """Level-order traversal using a queue."""
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self):
        """Preorder traversal (Root -> Left -> Right) using recursion."""
        result = []
        self._dfs_visit(self.root, result)
        return result

    def _dfs_visit(self, node, result):
        if node is None:
            return
        result.append(node.data)
        self._dfs_visit(node.left, result)
        self._dfs_visit(node.right, result)


def run():
    """Build the tree and print its traversals."""
    tree = BinaryTree()
    tree.build()
    print("=== BINARY TREE ===")
    print("DFS:", " - ".join(tree.dfs()))
    print("BFS:", " - ".join(tree.bfs()))


if __name__ == "__main__":
    run()

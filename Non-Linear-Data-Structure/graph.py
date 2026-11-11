"""
Graph structure (Assessment 3.3) - RAMOS

Vertices (numbered as in the diagram): R(1), A(2), M(3), O(4), S(5)
Directed edges (a two-way arrow is stored as two edges):
    R <-> A, R <-> M, R -> O, A <-> O, M -> O, A -> S, M -> S
Neighbors are visited in the diagram's number order: R, A, M, O, S.
"""
from collections import deque

ORDER = ["R", "A", "M", "O", "S"]


class Graph:
    def __init__(self):
        self.adjacency = {}

    def add_vertex(self, vertex):
        self.adjacency.setdefault(vertex, [])

    def add_edge(self, source, target):
        """One-way edge: source -> target."""
        self.adjacency[source].append(target)

    def add_two_way_edge(self, a, b):
        """Two-way edge: a <-> b."""
        self.add_edge(a, b)
        self.add_edge(b, a)

    def build(self):
        """Build the graph from the diagram."""
        for vertex in ORDER:
            self.add_vertex(vertex)
        self.add_two_way_edge("R", "A")
        self.add_two_way_edge("R", "M")
        self.add_edge("R", "O")
        self.add_two_way_edge("A", "O")
        self.add_edge("M", "O")
        self.add_edge("A", "S")
        self.add_edge("M", "S")
        # visit neighbors in the diagram's number order
        for vertex in self.adjacency:
            self.adjacency[vertex].sort(key=ORDER.index)

    def bfs(self, start):
        """Breadth-first search using a queue and a visited set."""
        visited = {start}
        queue = deque([start])
        result = []
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            for neighbor in self.adjacency[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return result

    def dfs(self, start):
        """Depth-first search using recursion and a visited set."""
        result = []
        self._dfs_visit(start, set(), result)
        return result

    def _dfs_visit(self, vertex, visited, result):
        visited.add(vertex)
        result.append(vertex)
        for neighbor in self.adjacency[vertex]:
            if neighbor not in visited:
                self._dfs_visit(neighbor, visited, result)


def run():
    """Build the graph and print its adjacency list and traversals."""
    graph = Graph()
    graph.build()
    print("=== GRAPH ===")
    for vertex, neighbors in graph.adjacency.items():
        print(f"{vertex}: {', '.join(neighbors) if neighbors else '-'}")
    print("DFS:", " - ".join(graph.dfs("R")))
    print("BFS:", " - ".join(graph.bfs("R")))


if __name__ == "__main__":
    run()

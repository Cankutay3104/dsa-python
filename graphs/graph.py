from collections import defaultdict, deque

class Graph:
    def __init__(self, directed=False):
        self.adj_list = defaultdict(list)
        self.directed = directed

    def add_edge(self, vertex1, vertex2):
        self.adj_list[vertex1].append(vertex2)
        if not self.directed:
            self.adj_list[vertex2].append(vertex1)

    def dfs(self, start_node):
        visited = set()
        traversal_order = []

        def _dfs(node):
            visited.add(node)
            traversal_order.append(node)

            for neighbor in self.adj_list[node]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start_node)
        return traversal_order

    def bfs(self, start_node):
        visited = set([start_node])
        queue = deque([start_node])
        distances = {start_node: 0}
        traversal_order = []

        while queue:
            curr = queue.popleft()
            traversal_order.append(curr)

            for neighbor in self.adj_list[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    distances[neighbor] = distances[curr] + 1
                    queue.append(neighbor)

        return traversal_order, distances
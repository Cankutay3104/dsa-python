# LeetCode "1971. Find if Path Exists in Graph" Solution

from collections import defaultdict, deque

class Solution(object):
    def validPath(self, n, edges, source, destination):
        if source == destination:
            return True

        adj_list = defaultdict(list)

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set([source])
        queue = deque([source])

        while queue:
            current = queue.popleft()

            if current == destination:
                return True

            for neighbor in adj_list[current]:
                if neighbor in visited:
                    continue

                if neighbor == destination:
                    return True

                visited.add(neighbor)
                queue.append(neighbor)

        return False
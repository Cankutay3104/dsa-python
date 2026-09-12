# LeetCode "133. Clone Graph" Solution

from collections import deque

# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None

        cloned = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            current = queue.popleft()

            for neighbor in current.neighbors:
                if neighbor not in cloned:
                    cloned[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)

                cloned[current].neighbors.append(cloned[neighbor])

        return cloned[node]
# LeetCode "637. Average of Levels in Binary Tree" Solution

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def averageOfLevels(root):
        if not root:
            print([])

        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            total = 0
            
            for _ in range(level_size):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(float(total)/level_size)

        return result
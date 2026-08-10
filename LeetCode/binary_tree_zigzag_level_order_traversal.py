# LeetCode "103. Binary Tree Zigzag Level Order Traversal" Solution

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        result = []
        level_count = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                if level_count % 2 == 0:
                    node = queue.popleft()
                    current_level.append(node.val)
                    
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                else:
                    node = queue.pop()
                    current_level.append(node.val)
                    
                    if node.right:
                        queue.appendleft(node.right)
                    if node.left:
                        queue.appendleft(node.left)

            result.append(current_level)
            level_count += 1

        return result
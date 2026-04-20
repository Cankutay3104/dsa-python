# LeetCode "110. Balanced Binary Tree" Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        return self._balanced_helper(root) != -1

    def _balanced_helper(self, node):
        if node is None:
            return 0
        
        left = self._balanced_helper(node.left)
        if left == -1:
            return -1

        right = self._balanced_helper(node.right)
        if right == -1:
            return -1
        
        if abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)
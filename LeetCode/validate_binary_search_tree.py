# LeetCode "98. Validate Binary Search Tree" Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        return self._bst_helper(root, float('-inf'), float('inf'))

    def _bst_helper(self, node, min_val, max_val):
        if node == None:
            return True
        elif node.val <= min_val or node.val >= max_val:
            return False
        else:
            return self._bst_helper(node.left, min_val, node.val) and self._bst_helper(node.right, node.val, max_val)
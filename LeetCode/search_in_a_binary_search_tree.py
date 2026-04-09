# LeetCode "700. Search in a Binary Search Tree"

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        current = root

        while current:
            if current.val < val:
                current = current.right
            elif current.val > val:
                current = current.left
            else:
                return current
        return None
# LeetCode "572. Subtree of Another Tree" Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):

        def isIdentical(first, second):
            if not first and not second:
                return True
            if not first or not second or first.val != second.val:
                return False
            return isIdentical(first.left, second.left) and isIdentical(first.right, second.right)

        if not subRoot:
            return True
        if not root:
            return False

        return isIdentical(root, subRoot) or self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot)

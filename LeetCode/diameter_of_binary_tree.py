# LeetCode "543. Diameter of Binary Tree" Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.max_diameter = 0

        def getHeight(node):
            if not node:
                return 0

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            self.max_diameter = max(self.max_diameter, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)

        getHeight(root)
        return self.max_diameter
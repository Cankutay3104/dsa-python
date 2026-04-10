# LeetCode "501.Find Mode in Binary Search Tree" Solution

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def findMode(self, root):
        if root is None:
            return []
        
        stack = []
        current = root

        modes = []
        prev_val = None
        current_occurrence = 0
        max_occurrence = 0

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            
            if current.val == prev_val:
                current_occurrence += 1
            else:
                current_occurrence = 1

            if current_occurrence > max_occurrence:
                max_occurrence = current_occurrence
                modes = [current.val]
            elif current_occurrence == max_occurrence:
                modes.append(current.val)
            
            prev_val = current.val
            current = current.right

        return modes
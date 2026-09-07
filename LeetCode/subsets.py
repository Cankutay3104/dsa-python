# LeetCode "78. Subsets" Solution

class Solution(object):
    def subsets(self, nums):
        result = []
        current_path = []

        def backtrack(idx):
            result.append(list(current_path))

            for i in range(idx, len(nums)):
                current_path.append(nums[i])
                backtrack(i + 1)
                current_path.pop()

        backtrack(0)
        return result
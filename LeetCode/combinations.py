# LeetCode "77. Combinations" Solution

class Solution(object):
    def combine(self, n, k):
        result = []
        current_path = []

        def backtrack(start):
            if len(current_path) == k:
                result.append(list(current_path))
                return

            for num in range(start, n + 1):
                current_path.append(num)
                backtrack(num + 1)
                current_path.pop()

        backtrack(1)
        return result
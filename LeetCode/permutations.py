# LeetCode "46. Permutations" Solution

class Solution(object):
    def permute(self, nums):
        result = []
        current_path = []
        visited = [False] * len(nums)

        def backtrack():
            if len(current_path) == len(nums):
                result.append(list(current_path))
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                visited[i] = True
                current_path.append(nums[i])

                backtrack()

                visited[i] = False
                current_path.pop()

        backtrack()
        return result
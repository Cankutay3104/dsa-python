# LeetCode "40. Combination Sum II" Solution

class Solution(object):
    def combinationSum2(self, candidates, target):
        result = []
        current_path = []
        candidates.sort()

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(list(current_path))
                return

            if remaining < 0:
                 return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                current_path.append(candidates[i])
                backtrack(i + 1, remaining - candidates[i])
                current_path.pop()

        backtrack(0, target)
        return result
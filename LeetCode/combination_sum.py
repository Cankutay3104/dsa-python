# LeetCode "39. Combination Sum" Solution

class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        current_path = []

        def backtrack(index, remaining):
            if remaining == 0:
                result.append(list(current_path))
                return

            if remaining < 0:
                return
                
            for i in range(index, len(candidates)):
                current_path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                current_path.pop()
            
        backtrack(0, target)
        return result
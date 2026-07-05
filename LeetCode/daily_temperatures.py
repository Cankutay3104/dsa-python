# LeetCode "739. Daily Temperatures" Solution

class Solution(object):
    def dailyTemperatures(self, temperatures):
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while len(stack) != 0 and temperatures[stack[-1]] < temp:
                past_day_index = stack.pop()
                
                wait_time = i - past_day_index
                answer[past_day_index] = wait_time
                
            stack.append(i)
        return answer
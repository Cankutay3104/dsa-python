# LeetCode "207. Course Schedule" Solution

from collections import defaultdict

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        adj_list = defaultdict(list)

        for course, prereq in prerequisites:
            adj_list[prereq].append(course)

        state = [0] * numCourses 

        def dfs(node):
            if state[node] == 1:
                # Cycle Found
                return False

            if state[node] == 2:
                return True

            state[node] = 1

            for neighbor in adj_list[node]:
                if not dfs(neighbor):
                    return False

            state[node] = 2
            return True

        for i in range(numCourses):
            if state[i] == 0:
                if not dfs(i):
                    return False

        return True
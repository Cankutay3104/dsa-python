# LeetCode "973. K Closest Points to Origin" Solution

import heapq

class Solution(object):
    def kClosest(self, points, k):

        max_heap = []
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(max_heap, (-dist, [x, y]))

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [point for (_, point) in max_heap]
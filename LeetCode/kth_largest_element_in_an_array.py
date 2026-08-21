# LeetCode "215. Kth Largest Element in an Array" Solution

import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]
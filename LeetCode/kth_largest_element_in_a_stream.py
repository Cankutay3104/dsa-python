# LeetCode "703. Kth Largest Element in a Stream" Solution

import heapq

class KthLargest(object):

    def __init__(self, k, nums):
        self.largest = k
        self.heap = nums

        heapq.heapify(self.heap)
        while len(self.heap) > self.largest:
            heapq.heappop(self.heap)
        
    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.largest:
            heapq.heappop(self.heap)
        return self.heap[0]
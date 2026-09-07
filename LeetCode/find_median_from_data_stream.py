# LeetCode "295. Find Median From Data Stream" Solution

import heapq

class MedianFinder(object):

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num):
        heapq.heappush(self.small, -num)

        if self.small and self.large and (-self.small[0] > self.large[0]):
            out = -heapq.heappop(self.small)
            heapq.heappush(self.large, out)

        if len(self.small) > len(self.large) + 1: 
            out = -heapq.heappop(self.small)
            heapq.heappush(self.large, out)

        if len(self.large) > len(self.small):
            out = heapq.heappop(self.large)
            heapq.heappush(self.small, -out)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0

# LeetCode "347. Top K Frequent Elements" Solution

class Solution(object):
    def topKFrequent(self, nums, k):
        elementMap = {}

        for el in nums:
            if el not in elementMap:
                elementMap[el] = 0
            elementMap[el] += 1

        bucket = [[] for _ in range(len(nums) + 1)]
        
        for key, value in elementMap.items():
            bucket[value].append(key)
        
        result = []
        counter = 0
        for i in range(len(bucket), 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
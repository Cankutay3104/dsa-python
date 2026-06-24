# LeetCode '560. Subarray Sum Equals K' Solution

class Solution(object):
    def subarraySum(self, nums, k):
        counts = {}
        counts[0] = 1

        total_subarrays = 0
        sum = 0

        for num in nums:
            sum += num
            target = sum - k

            if target in counts:
                total_subarrays += counts[target]
            
            if sum in counts:
                counts[sum] += 1
            else:
                counts[sum] = 1
        
        return total_subarrays
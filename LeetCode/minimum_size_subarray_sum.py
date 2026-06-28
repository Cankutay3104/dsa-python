# LeetCode "209. Minimum Size Subarray Sum" Solution

class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        cur_sum = 0
        size = 0
        min_size = float('inf')

        for i, num in enumerate(nums):
            cur_sum += num
            size = i - left + 1

            while cur_sum >= target:
                if size < min_size:
                    min_size = size
                
                cur_sum -= nums[left]
                left += 1
                size -= 1
        
        if min_size == float('inf'):
            return 0
        return min_size
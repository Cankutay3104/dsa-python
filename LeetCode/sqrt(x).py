# LeetCode "69. Sqrt(x)" Solution

class Solution(object):
    def mySqrt(self, x):
        low = 0
        high = x

        while low <= high:
            mid = (high + low) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            elif mid * mid > x:
                high = mid - 1
                
        return high
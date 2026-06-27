# LeetCode "42. Trapping Rain Water" Solution

class Solution(object):
    def trap(self, height):
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]
        total_unit_water = 0

        while left < right:
            if height[left] <= height[right]:
                if max_left <= height[left]:
                    max_left = height[left]
                else:
                    total_unit_water += max_left - height[left]
                left += 1
            else:
                if max_right <= height[right]:
                    max_right = height[right]
                else:
                    total_unit_water += max_right - height[right]
                right -= 1
        
        return total_unit_water
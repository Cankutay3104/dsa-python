# LeetCode "74. Search a 2D Matrix" Solution

class Solution(object):
    def searchMatrix(self, matrix, target):
        total_col = len(matrix[0])
        total_row = len(matrix)
        left = 0
        right = total_col * total_row - 1

        while left <= right:
            mid = left + (right - left) // 2
            cur_col = mid % total_col
            cur_row = mid // total_col

            if matrix[cur_row][cur_col] == target:
                return True
            elif matrix[cur_row][cur_col] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
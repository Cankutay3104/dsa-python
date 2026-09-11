# LeetCode "200. Number of Islands" Solution

from collections import deque

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0
        
        island_count = 0
        rows = len(grid)
        cols = len(grid[0])

        def bfs(row, col):
            queue = deque([(row, col)])
            grid[row][col] = "0"

            while queue:
                curr_row, curr_col = queue.popleft()

                if curr_col + 1 < cols and grid[curr_row][curr_col + 1] == "1":
                    grid[curr_row][curr_col + 1] = "0"
                    queue.append((curr_row, curr_col + 1))

                if curr_row + 1 < rows and grid[curr_row + 1][curr_col] == "1":
                    grid[curr_row + 1][curr_col] = "0"
                    queue.append((curr_row + 1, curr_col))

                if curr_col - 1 >= 0 and grid[curr_row][curr_col - 1] == "1":
                    grid[curr_row][curr_col - 1] = "0"
                    queue.append((curr_row, curr_col - 1))

                if curr_row - 1 >= 0 and grid[curr_row - 1][curr_col] == "1":
                    grid[curr_row - 1][curr_col] = "0"
                    queue.append((curr_row - 1, curr_col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    island_count += 1
                    bfs(row, col)

        return island_count
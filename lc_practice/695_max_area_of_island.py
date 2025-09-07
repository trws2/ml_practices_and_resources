# runtime: O(m x n)
# space: O(m x n)

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if i >= rows or j >= cols:
                return 0
            if grid[i][j] in (0, 2):
                return 0

            grid[i][j] = 2
            area = 1
            area += dfs(i+1, j)
            area += dfs(i-1, j)
            area += dfs(i, j+1)
            area += dfs(i, j-1)

            return area

        max_area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in (0, 2):
                    continue
                area = dfs(i, j)
                if max_area < area:
                    max_area = area

        return max_area

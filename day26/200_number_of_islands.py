# runtime: O(m x n)
# space: O(m x n)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid: List[List[str]], i, j):
            if i < 0 or j < 0:
                return
            if i >= len(grid) or j >= len(grid[0]):
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(grid, i-1, j)
            dfs(grid, i+1, j)
            dfs(grid, i, j-1)
            dfs(grid, i, j+1)                                    
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid, i, j)

        return res


# runtime: O(m x n)
# space: O(m x n)

# newer implementation
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            if i < 0 or j < 0:
                return
            if i >= rows or j >= cols:
                return
            if grid[i][j] in ('0', '2'):
                return

            grid[i][j] = '2'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in ('0', '2'):
                    continue
                dfs(i, j)
                count += 1
        
        return count



# older implementation
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



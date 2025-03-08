# runtime: O(rows x cols)
# space: O(rows x cols)

from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        res = 0
        prev_level = -1
        while queue:
            row, col, level = queue.popleft()

            step_forward = False
            # print(f"A: row={row}, col={col}, grid={grid}")

            if row-1 >= 0 and grid[row-1][col] == 1:
                grid[row-1][col] = 2
                queue.append((row-1, col, level+1))
                step_forward = True                
            if col-1 >= 0 and grid[row][col-1] == 1:
                grid[row][col-1] = 2
                queue.append((row, col-1, level+1))                
                step_forward = True                
            if row+1 < rows and grid[row+1][col] == 1:
                grid[row+1][col] = 2
                queue.append((row+1, col, level+1))
                step_forward = True                
            if col+1 < cols and grid[row][col+1] == 1:
                grid[row][col+1] = 2
                queue.append((row, col+1, level+1))
                step_forward = True

            if step_forward and level > prev_level:
                res += 1
                prev_level = level

            # print(f"B: row={row}, col={col}, step_forward={step_forward}, grid={grid}, res={res}")

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return res


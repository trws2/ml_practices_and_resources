# runtime: log(m x n)
# space: log(1)

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols - 1

        while left <= right:
            mid = int((left + right) / 2)

            row_index = int(mid / cols)
            col_index = mid % cols

            val = matrix[row_index][col_index]

            if val == target:
                return True
            
            if val < target:
                left = mid + 1 
                continue

            right = mid - 1

        return False


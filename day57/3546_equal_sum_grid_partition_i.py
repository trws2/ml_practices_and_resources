class Solution:

    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def compute_integral_image(grid: List[List[int]]) -> List[List[int]]:
            # integral_im[i][j] = grid[i][j] + integral_im[i-1][j] + integral_im[i][j-1] - integral_im[i-1][j-1]
            integral_im = [[0 for _ in range(cols)] for _ in range(rows)]

            integral_im[0][0] = grid[0][0]
            for i in range(1, rows):
                integral_im[i][0] = grid[i][0] + integral_im[i-1][0]

            for j in range(1, cols):
               integral_im[0][j] = grid[0][j] + integral_im[0][j-1]

            for i in range(1, rows):
                for j in range(1, cols):
                    integral_im[i][j] = grid[i][j] + integral_im[i-1][j] + integral_im[i][j-1] - integral_im[i-1][j-1]

            return integral_im

        rows = len(grid)
        cols = len(grid[0])
        integral_im = compute_integral_image(grid)

        total_area_sum = integral_im[rows-1][cols-1]

        if total_area_sum % 2 != 0:
            return False
        
        target_sub_area_sum = total_area_sum / 2

        # horizonal cut
        for i in range(rows-1):
            if integral_im[i][cols-1] == target_sub_area_sum:
                return True
            elif integral_im[i][cols-1] > target_sub_area_sum:
                break

        # vertical cut
        for i in range(cols-1):
            if integral_im[rows-1][i] == target_sub_area_sum:
                return True
            elif integral_im[rows-1][i] > target_sub_area_sum:
                break

        return False


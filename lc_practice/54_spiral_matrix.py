# runtime: O(M x N)
# space: O(M x N)

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        visited_count = 0
        rows = len(matrix)
        cols = len(matrix[0])        
        target_count = rows * cols

        def move_left(cur_col, cur_row):
            if cur_col+1 < cols and visited[cur_row][cur_col+1] == False:
                cur_col += 1
                prev_direction = 1
                return (cur_row, cur_col, prev_direction)
            return (None, None, None)

        def move_down(cur_col, cur_row):
            if cur_row+1 < rows and visited[cur_row+1][cur_col] == False:
                cur_row += 1
                prev_direction = 2
                return (cur_row, cur_col, prev_direction)
            return (None, None, None)            

        def move_right(cur_col, cur_row):
            if cur_col-1 >= 0 and visited[cur_row][cur_col-1] == False:
                cur_col -= 1
                prev_direction = 3
                return (cur_row, cur_col, prev_direction)
            return (None, None, None)

        def move_up(cur_col, cur_row):
            if cur_row-1 >= 0 and visited[cur_row-1][cur_col] == False:
                cur_row -= 1
                prev_direction = 4
                return (cur_row, cur_col, prev_direction)
            return (None, None, None)

        ret = []
        cur_row = 0
        cur_col = 0
        prev_direction = 1
        while True:
            ret.append(matrix[cur_row][cur_col])
            visited[cur_row][cur_col] = True
            visited_count += 1
            if visited_count == target_count:
                break
            if prev_direction == 1:
                tmp_cur_row, tmp_cur_col, prev_direction = move_left(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_down(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue                    
                tmp_cur_row, tmp_cur_col, prev_direction = move_right(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_up(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue

            elif prev_direction == 2:
                tmp_cur_row, tmp_cur_col, prev_direction = move_down(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col
                    continue                    
                tmp_cur_row, tmp_cur_col, prev_direction = move_right(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_up(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_left(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue

            elif prev_direction == 3:
                tmp_cur_row, tmp_cur_col, prev_direction = move_right(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_up(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_left(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_down(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue                    

            elif prev_direction == 4:
                tmp_cur_row, tmp_cur_col, prev_direction = move_up(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_left(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue
                tmp_cur_row, tmp_cur_col, prev_direction = move_down(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue                    
                tmp_cur_row, tmp_cur_col, prev_direction = move_right(cur_col, cur_row)
                if prev_direction:
                    cur_row = tmp_cur_row
                    cur_col = tmp_cur_col                    
                    continue

        return ret


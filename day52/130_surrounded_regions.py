# runtime: O(n^2)
# space: O(n^2)

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_surrounded(i, j):
            res = True

            if i == rows - 1 or j == cols - 1:
                res = False
            
            if i == 0 or j == 0:
                res = False

            # being visit
            visit_status[i][j] = 1

            dir_x = i-1
            dir_y = j
            if dir_x >= 0 and visit_status[dir_x][dir_y] == 0 and board[dir_x][dir_y] == 'O':
                tmp = is_surrounded(dir_x, dir_y)
                res = res and tmp

            dir_x = i+1
            dir_y = j
            if dir_x < rows and visit_status[dir_x][dir_y] == 0 and board[dir_x][dir_y] == 'O':
                tmp = is_surrounded(dir_x, dir_y)
                res = res and tmp

            dir_x = i
            dir_y = j-1
            if dir_y >= 0 and visit_status[dir_x][dir_y] == 0 and board[dir_x][dir_y] == 'O':
                tmp = is_surrounded(dir_x, dir_y)
                res = res and tmp

            dir_x = i
            dir_y = j+1
            if dir_y < cols and visit_status[dir_x][dir_y] == 0 and board[dir_x][dir_y] == 'O':
                tmp = is_surrounded(dir_x, dir_y)
                res = res and tmp

            # done visiting
            visit_status[i][j] = 2
            all_nodes.append((i, j))
            return res

        rows = len(board)
        cols = len(board[0])
        visit_status = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if visit_status[i][j] == 0 and board[i][j] == 'O':
                    all_nodes = []
                    if is_surrounded(i, j):
                        for node in all_nodes:
                            board[node[0]][node[1]] = 'X'


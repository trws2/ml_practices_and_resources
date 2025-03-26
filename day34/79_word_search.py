# runtime: O(M x N x |word|)
# space: O(M x N x |word|)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        def dfs(board, visiting, target_word, current_word, i, j):
            if i < 0 or i >= len(board):
                return False

            if j < 0 or j >= len(board[0]):
                return False

            if visiting[i][j] == True:
                return False

            current_word += board[i][j]
            visiting[i][j] = True

            if target_word == current_word:
                return True

            if not target_word.startswith(current_word):
                visiting[i][j] = False
                current_word = current_word[:-1]
                return False

            ret1 = dfs(board, visiting, target_word, current_word, i+1, j)
            if ret1:
                return True
            ret2 = dfs(board, visiting, target_word, current_word, i-1, j)
            if ret2:
                return True            
            ret3 = dfs(board, visiting, target_word, current_word, i, j+1)
            if ret3:
                return True            
            ret4 = dfs(board, visiting, target_word, current_word, i, j-1)            
            if ret4:
                return True

            visiting[i][j] = False
            current_word = current_word[:-1]

            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                visiting = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
                if dfs(board, visiting, word, "", i, j):
                    return True

        return False

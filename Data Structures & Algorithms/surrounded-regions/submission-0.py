class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
            if ((r < 0 or r >= ROWS) 
            or (c < 0 or c >= COLS) 
            or (board[r][c] == 'X') 
            or (board[r][c] == 'B')):
                return
            if board[r][c] == 'O':
                board[r][c] = 'B'
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        for c in range(COLS):
            dfs(0, c)
            dfs(ROWS - 1, c)
        for r in range(1, ROWS - 1): # skips corners
            dfs(r, 0)
            dfs(r, COLS - 1)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'B':
                    board[r][c] = 'O'
        
        
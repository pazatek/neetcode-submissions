class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for i in range(m)]
        def dp(r, c, rows, cols, memo):
            if r == rows or c == cols:
                return 0
            if  memo[r][c] > 0:
                return memo[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            memo[r][c] = dp(r+1, c, rows, cols, memo) + dp(r, c+1, rows, cols, memo)
            return memo[r][c]
        return dp(0, 0, m, n, memo)
        
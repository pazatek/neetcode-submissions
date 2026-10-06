class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0] * n for i in range(m)]
        def dp(r, c):
            if r == m or c == n:
                return 0
            if  memo[r][c] > 0:
                return memo[r][c]
            if r == m - 1 and c == n - 1:
                return 1
            memo[r][c] = dp(r+1, c) + dp(r, c+1)
            return memo[r][c]
        return dp(0, 0)
        
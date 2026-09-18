class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        memo = [[-1] * cols for i in range(rows)]
        def dp(r, c, rows, cols, memo):
            if r == rows or c == cols or obstacleGrid[r][c] == 1:
                return 0
            if  memo[r][c] > -1:
                return memo[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            memo[r][c] = dp(r+1, c, rows, cols, memo) + dp(r, c+1, rows, cols, memo)
            return memo[r][c]
        return dp(0, 0, rows, cols, memo)
        
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        self.paths = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(r,c):
            if ((r < 0 or r >= ROWS) 
            or (c < 0 or c >= COLS) 
            or ((r,c) in visited) 
            or (grid[r][c] == 1)):
                return
            if (r == ROWS - 1) and (c == COLS - 1):
                self.paths += 1
                return
            visited.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            visited.remove((r,c))
        dfs(0,0)
        return self.paths

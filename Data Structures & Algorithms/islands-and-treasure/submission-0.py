class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while q:
            r, c = q.popleft()
            for rowDiff, colDiff in directions:
                row, col = r + rowDiff, c + colDiff
                if ((row < 0 or row >= ROWS or col < 0 or col >= COLS) or (grid[row][col] != 2147483647)):
                    continue
                grid[row][col] = grid[r][c] + 1
                q.append((row,col))




                
    

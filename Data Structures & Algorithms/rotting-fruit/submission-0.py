class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        fresh = 0
        time = 0
        
        for r in range (ROWS):
            for c in range (COLS):
                if grid[r][c] == 2:
                    queue.append([r,c])
                if grid[r][c] == 1:
                    fresh += 1
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while queue and fresh > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()
                for rowDiff, colDiff in directions:
                    row, col = r + rowDiff, c + colDiff
                    if (row < 0 or row >= len(grid) or
                        col < 0 or col >= len(grid[0]) or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row, col])
                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1
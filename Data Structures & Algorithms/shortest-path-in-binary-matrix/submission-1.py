class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        queue = deque()
        queue.append((0,0))
        visited.add((0,0))

        length = 1
        if grid[0][0] == 1:
            return -1
        while queue:
            for i in range (len(queue)):
                r, c = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return length
                
                neighbors = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

                for rowDiff, colDiff in neighbors:
                    if r + rowDiff < 0 or c + colDiff < 0 or r + rowDiff >= ROWS or c + colDiff >= COLS or (r + rowDiff, c + colDiff) in visited or grid[r + rowDiff][c + colDiff] == 1:
                        continue
                    queue.append((r + rowDiff, c + colDiff))
                    visited.add((r + rowDiff, c + colDiff))
            length += 1      
        return -1  
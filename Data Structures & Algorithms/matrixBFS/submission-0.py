class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        q.append((0,0))
        ROWS = len(grid)
        COLS = len(grid[0])
        length = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                if (r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or ((r,c) in visited) or (grid[r][c] == 1):
                    continue
                visited.add((r,c))
                if (r == ROWS - 1) and (c == COLS - 1):
                    return length
                q.append((r+1,c))
                q.append((r-1,c))
                q.append((r,c+1))
                q.append((r,c-1))   
            length += 1
        return -1
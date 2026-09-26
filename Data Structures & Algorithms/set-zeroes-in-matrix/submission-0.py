class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        zeroOut = set()
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    zeroOut.add((r,c))
        for row, col in zeroOut:
            for c in range(COLS):
                matrix[row][c] = 0
            for r in range(ROWS):
                matrix[r][col] = 0


        
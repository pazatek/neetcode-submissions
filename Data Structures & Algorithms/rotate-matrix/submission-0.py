class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # 1 2 3
        # 4 5 6
        # 7 8 9

        # 7 8 9
        # 4 5 6
        # 1 2 3

        # 7 4 1
        # 8 5 2
        # 9 6 3

        ROWS = len(matrix)
        COLS = len(matrix[0])

        # swap rows
        for row in range(ROWS // 2):
            temp = matrix[row]
            matrix[row] = matrix[ROWS - 1 - row]
            matrix[ROWS - 1 - row] = temp
        
        for row in range(ROWS):
            for col in range(COLS):
                if row < col:
                    temp = matrix[row][col]
                    matrix[row][col] = matrix[col][row]
                    matrix[col][row] = temp



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        top = 0
        bottom = ROWS - 1
        left = 0
        right = COLS - 1

        # [1,2,3,4],
        # [5,6,7,8],
        # [9,10,11,12]
        output = []
        while (top <= bottom) and (left <= right):
            for col in range(left, right + 1):
                output.append(matrix[top][col])
            top += 1
            for row in range(top, bottom + 1):
                output.append(matrix[row][right])
            right -= 1
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    output.append(matrix[bottom][col])
                bottom -= 1
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    output.append(matrix[row][left])
                left += 1
        return output



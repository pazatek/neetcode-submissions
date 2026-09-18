class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            midrow = (left + right) // 2
            if target > matrix[midrow][-1]:
                left = midrow + 1
            elif target < matrix[midrow][0]:
                right = midrow - 1
            else:
                left = 0
                right = len(matrix[midrow]) - 1
                while left <= right:
                    midpoint = (left + right) // 2
                    if target < matrix[midrow][midpoint]:
                        right = midpoint - 1
                    elif target > matrix[midrow][midpoint]:
                        left = midpoint + 1
                    else:
                        return True
                return False
        return False
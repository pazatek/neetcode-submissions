class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check each row
        for r in range(len(board)):
            seenInRow = set()
            for c in range(len(board[0])):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seenInRow:
                    return False
                else:
                    seenInRow.add(board[r][c])
        # check each col
        for c in range(len(board[0])):
            seenInCol = set()
            for r in range(len(board)):
                if board[r][c] == '.':
                    continue
                if board[r][c] in seenInCol:
                    return False
                else:
                    seenInCol.add(board[r][c]) 
        # check each square
        for boxrow in range(3):
            for boxcol in range(3):
                seenInBox = set()
                for r in range(3):
                    for c in range(3):
                        if board[boxrow*3+r][boxcol*3+c] == '.':
                            continue
                        if board[boxrow*3+r][boxcol*3+c] in seenInBox:
                            return False
                        else:
                            seenInBox.add(board[boxrow*3+r][boxcol*3+c])
        return True
        


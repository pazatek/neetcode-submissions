class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        def checkIfNextLetter(r,c,stringIndex):

            if stringIndex > (len(word) - 1):
                return True

            if ((r >= ROWS or r < 0 or c >= COLS or c < 0)
            or (board[r][c] != word[stringIndex]) 
            or (board[r][c] == 1)):
                return False

            # mark curr square as visited
            originalChar = board[r][c]
            board[r][c] = 1

            # check surrounding
            found = (checkIfNextLetter(r+1,c,stringIndex+1) or 
            checkIfNextLetter(r-1,c,stringIndex+1) or 
            checkIfNextLetter(r,c+1,stringIndex+1) or 
            checkIfNextLetter(r,c-1,stringIndex+1))
            
            # restore visited
            board[r][c] = originalChar

            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if checkIfNextLetter(r,c,0):
                        return True
        return False
                    


        
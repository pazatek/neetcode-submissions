class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # begin with starting pixel and change its color
        ogColor = image[sr][sc]
        if color == ogColor:
            return image

        def dfs(r, c):
            if r >= len(image) or c >= len(image[0]) or r < 0 or c < 0 or image[r][c] != ogColor:
                return
            image[r][c] = color

            dfs(r + 1, c) # up
            dfs(r - 1, c) # down
            dfs (r, c - 1) # left
            dfs (r, c + 1) # right
        dfs(sr, sc)
        return image
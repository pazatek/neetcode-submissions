class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.word
    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True
    def startsWith(self, prefix):
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True
    
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ROWS = len(board)
        COLS = len(board[0])
        result = set()
        visited = set()
        trie = Trie()
        for word in words:
            trie.add(word)
        def dfs(r, c, node, path):
            if ((r < 0 or r >= ROWS) or (c < 0 or c >= COLS) or
            (board[r][c] not in node.children) or
            ((r,c) in visited)):
                return
            node = node.children[board[r][c]]
            if node.word:
                result.add(path + board[r][c])
            visited.add((r,c))
            dfs(r+1,c,node, path + board[r][c])
            dfs(r-1,c,node, path + board[r][c])
            dfs(r,c+1,node, path + board[r][c])
            dfs(r,c-1,node, path + board[r][c])
            visited.remove((r,c))
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, trie.root, "")
        return list(result)









        
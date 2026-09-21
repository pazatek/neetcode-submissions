class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index == len(s):
                return True
            for word in wordDict:
                if (s[index:index + len(word)] == word) and dfs(index + len(word)):
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        return dfs(0)
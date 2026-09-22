class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        strings = []
        string = []
        digitToChars = {'2': ['a','b','c'], '3': ['d','e','f'],
                      '4': ['g','h','i'], '5': ['j','k','l'], '6': ['m','n','o'],
                      '7': ['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        def dfs(index):
            if index == len(digits):
                strings.append(''.join(string))
                return
            for char in digitToChars[digits[index]]:
                string.append(char)
                dfs(index + 1)
                string.pop()
        dfs(0)
        return strings if digits else []
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # We can add a closer if unclosed > 0. We can add a ( if openers < n.
        valids = []
        path = ""
        def dfs(unclosed, openers, path):
            if unclosed > 0:
                dfs(unclosed - 1, openers, path + ")")
            if openers < n:
                dfs(unclosed + 1, openers + 1, path + "(")
            if unclosed == 0 and openers == n:
                valids.append(path)
        dfs(0,0,path)
        return valids


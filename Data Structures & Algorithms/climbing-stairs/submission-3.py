class Solution:
    def climbStairs(self, n: int) -> int:
        waysPerNumber = {}
        def dp(n):
            if n in waysPerNumber:
                return waysPerNumber[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            else:
                waysPerNumber[n] = dp(n-1) + dp(n-2)
                return waysPerNumber[n]
        return dp(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}
        def subDecode(i):
            if i in memo:
                return memo[i]

            if i == len(s):
                return 1
            elif s[i] == '0':
                return 0

            elif (int(s[i:i+2]) > 26) or (i + 1 == len(s)):
                memo[i] = subDecode(i + 1)
            else:
                memo[i] = subDecode(i + 1) + subDecode(i + 2)
            return memo[i]
        return subDecode(0)


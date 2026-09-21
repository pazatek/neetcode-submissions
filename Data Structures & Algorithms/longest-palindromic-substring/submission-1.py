class Solution:
    def longestPalindrome(self, s: str) -> str:
        subStart = 0
        subEnd = 0

        def iterate(left, right):
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                    left -= 1
                    right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            left = i - 1
            right = i + 1
            left, right = iterate(left, right)
            if right - left + 1 > subEnd - subStart + 1:
                subStart = left
                subEnd = right

            left = i
            right = i + 1
            left, right = iterate(left, right)
            if right - left + 1 > subEnd - subStart + 1:
                subStart = left
                subEnd = right

        return s[subStart:subEnd + 1]

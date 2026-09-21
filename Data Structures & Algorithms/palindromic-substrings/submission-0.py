class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def iterate(left, right, count):                
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        for i in range(len(s)):
            count += iterate(i, i + 1, 0)
            count += iterate(i - 1, i + 1, 1)
        return count


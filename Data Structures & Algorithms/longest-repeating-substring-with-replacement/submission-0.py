class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        length = 0
        charCounts = {}
        for right in range(len(s)):
            if s[right] in charCounts:
                charCounts[s[right]] += 1
            else:
                charCounts[s[right]] = 1
            while ((right-left+1) - max(charCounts.values())) > k:
                charCounts[s[left]] -= 1
                left += 1
            length = max(length, (right-left+1))
        return length
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sCounts = {}
        tCounts = {}
        for char in s:
            if char in sCounts:
                sCounts[char] += 1
            else:
                sCounts[char] = 1
        for char in t:
            if char in tCounts:
                tCounts[char] += 1
            else:
                tCounts[char] = 1
        return sCounts == tCounts


        
        
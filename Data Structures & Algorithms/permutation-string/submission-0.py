class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        charCount = {}
        for i in range(len(s1)):
            if s1[i] in charCount:
                charCount[s1[i]] += 1
            else:
                charCount[s1[i]] = 1
        left = 0
        right = len(s1) - 1

        windowCount = {}
        for i in range(left, right + 1):
            if s2[i] in windowCount:
                windowCount[s2[i]] += 1
            else:
                windowCount[s2[i]] = 1
    
        while right < len(s2):
            if windowCount == charCount:
                return True
            
            windowCount[s2[left]] -= 1
            if windowCount[s2[left]] == 0:
                windowCount.pop(s2[left])
            left += 1
            right += 1
            if right == len(s2):
                return False
            if s2[right] in windowCount:
                windowCount[s2[right]] += 1
            else:
                windowCount[s2[right]] = 1
        return False

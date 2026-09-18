class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tCharCount = {}
        for char in t:
            if char in tCharCount:
                tCharCount[char] += 1
            else:
                tCharCount[char] = 1
        
        window = {}
        
       
        need = len(tCharCount)
        have = 0

        left = 0
        right = 0
        minLength = float('inf')
        leftIndex = 0
        rightIndex = 0
        for right in range(len(s)):
            newChar = s[right]
            if newChar in window:
                window[newChar] += 1
            else:
                window[newChar] = 1

            if newChar in tCharCount and tCharCount[newChar] == window[newChar]:
                have += 1
            while have == need:
                newLength = (right - left) + 1
                if newLength < minLength:
                    minLength = newLength
                    leftIndex = left
                    rightIndex = right
                oldChar = s[left]
                if (oldChar in tCharCount) and (window[oldChar] == tCharCount[oldChar]):
                    have -= 1
                window[oldChar] -= 1
                left += 1

        return s[leftIndex:rightIndex + 1] if minLength != float('inf') else ""
            
                
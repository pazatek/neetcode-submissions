class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        partitions = []
        def isPalindrome(substring):
            left = 0
            right = len(substring) - 1
            while left < right:
                if substring[left] != substring[right]:
                    return False
                right -= 1
                left += 1
            return True

        def dfs(i):
            if i >= len(s):
                results.append(partitions.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s[i:j + 1]):
                    partitions.append(s[i:j + 1])
                    dfs(j + 1)
                    partitions.pop()



        dfs(0)
        return results
            
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest = 0
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            longest = 1
            for i in range(index + 1, len(nums)):
                if (nums[i] > nums[index]):
                   longest = max(1 + dfs(i), longest)
            memo[index] = longest
            return longest
        return max(dfs(i) for i in range(len(nums)))
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(index):
            if index in memo:
                return memo[index]
            if index >= len(nums) - 1:
                return True
            for jump in range(1, nums[index] + 1):
                if dfs(index + jump) == True:
                    memo[index] = True
                    return True
            memo[index] = False
            return False
        return dfs(0)
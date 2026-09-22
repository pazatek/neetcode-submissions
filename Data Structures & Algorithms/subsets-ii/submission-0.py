class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        nums.sort()
        def dfs(i):                
            if i >= len(nums):
                result.append(subset.copy())
                return
            # add current
            subset.append(nums[i])
            dfs(i + 1)
            # dont add current
            current = subset.pop()
            while i < len(nums) and nums[i] == current:
                i += 1
            dfs(i)
        dfs(0)
        return result
            
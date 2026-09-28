class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        path = []
        paths = []
        def dfs(i,currSum):
            if currSum == target:
                paths.append(path.copy())
                return
            if currSum > target or i == len(nums):
                return
            
            
            # add this value
            path.append(nums[i])
            dfs(i + 1, currSum + nums[i])
            # don't add this value (or its duplicated)
            path.pop()
            duped = nums[i]
            while i < len(nums) and nums[i] == duped:
                i += 1
            dfs(i, currSum)
        dfs(0,0)
        return paths
            

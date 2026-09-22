class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # add curr
            subset.append(nums[i])
            dfs(i + 1)

            # dont add curr
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result

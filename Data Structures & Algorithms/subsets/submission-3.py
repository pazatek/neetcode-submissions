class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        subset = []
        # [1,2,2]
        # [1,2,2],[1,2]
        def dfs(i):
            if i >= len(nums):
                result.append(subset.copy())
                return
            # add this value
            subset.append(nums[i])
            dfs(i + 1)

            # don't add this value
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return result

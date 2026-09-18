class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        sumPath = []
        def dfs(i, sum):
            if sum == target:
                results.append(sumPath.copy())
                return
            if i >= len(nums) or sum > target:
                return

            
            sumPath.append(nums[i])
            dfs(i, sum + nums[i])
            # dont add next value
            sumPath.pop()
            dfs(i + 1, sum)

        dfs(0, 0)
        return results

        
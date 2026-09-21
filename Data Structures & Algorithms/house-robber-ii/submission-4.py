class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def subRob(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 0:
                return 0

            twoBack = nums[0]
            oneBack = max(nums[1], nums[0])

            for i in range(2, len(nums)):
                best = max(twoBack + nums[i], oneBack)
                twoBack = oneBack
                oneBack = best
            return oneBack
        return max(subRob(nums[1:]), subRob(nums[:-1]))
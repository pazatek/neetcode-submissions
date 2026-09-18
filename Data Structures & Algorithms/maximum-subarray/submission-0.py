class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestOverall = nums[0]
        bestRightNow = nums[0]
        for i in range (1, len(nums)):
            bestRightNow = max(nums[i], bestRightNow + nums[i])
            bestOverall = max(bestRightNow, bestOverall)
        return bestOverall
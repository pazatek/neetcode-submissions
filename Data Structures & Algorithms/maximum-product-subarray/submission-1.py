class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        bestOverall = nums[0]
        bestRightNow = nums[0]
        smallest = nums[0]
        for i in range(1, len(nums)):
            temp = smallest
            smallest = min(nums[i], bestRightNow * nums[i], smallest * nums[i])
            bestRightNow = max(nums[i], bestRightNow * nums[i], temp * nums[i])
            bestOverall = max(bestOverall, bestRightNow)
        return bestOverall
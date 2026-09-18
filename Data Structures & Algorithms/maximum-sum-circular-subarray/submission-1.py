class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            curSum = max(nums[i], curSum + nums[i])
            maxSum = max(curSum, maxSum)
        minSum = nums[0]
        curSum = nums[0]
        for i in range(1, len(nums)):
            curSum = min(nums[i], curSum + nums[i])
            minSum = min(curSum, minSum)
        # minSum now has the subarray with the lowest value possible
        if maxSum < 0:
            return maxSum
        wrappedSum = sum(nums) - minSum
        return max(wrappedSum, maxSum)

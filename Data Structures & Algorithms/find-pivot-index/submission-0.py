class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixSums = [0] * len(nums)
        postfixSums = [0] * len(nums)
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            prefixSums[i] = total
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            postfixSums[i] = total
        for i in range(len(nums)):
            if postfixSums[i] - prefixSums[i] == 0:
                return i
        return -1


            
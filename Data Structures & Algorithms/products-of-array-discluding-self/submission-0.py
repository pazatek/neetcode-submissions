class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # product of all before it
        # product of all after it
        before = [1] * len(nums)
        after = [1] * len(nums)

        # [1,2,4,6] nums
        # [1,1,1,1] before
        for i in range(1, len(nums)):
            before[i] = nums[i - 1] * before[i - 1]
        # [1,2,4,6] nums
        # [2,1,1,1] after
        for i in range(len(nums) - 2, -1, -1):
            after[i] = nums[i + 1] * after[i + 1]


        out = [1] * len(nums)
        for i in range(len(out)):
            out[i] = (before[i] * after[i])
        return out

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthestIndex = 0
        for i in range(len(nums)):
            if i > furthestIndex:
                return False
            if i + nums[i] > furthestIndex:
                furthestIndex = i + nums[i]
        if furthestIndex >= len(nums) - 1:
            return True
        else: 
            return False
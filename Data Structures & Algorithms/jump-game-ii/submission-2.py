class Solution:
    def jump(self, nums: List[int]) -> int:
        maxIndex = nums[0]
        possibleJump = nums[0]
        jumps = 0
        if len(nums) == 1:
            return 0
        for i in range(len(nums)):
            if maxIndex >= len(nums) - 1:
                return jumps + 1
            if nums[i] + i > possibleJump:
                possibleJump = i + nums[i]
            if i == maxIndex:
                maxIndex = possibleJump
                jumps += 1
            
        return jumps
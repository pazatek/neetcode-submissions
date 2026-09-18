class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        Highest = 0
        CurrentMax = 0
        for num in nums:
            if num == 1:
                 CurrentMax += 1
                 if CurrentMax >= Highest:
                    Highest = CurrentMax
            if num == 0:
                CurrentMax = 0
        return Highest
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        majority = 0
        count = 0
        majority2 = 0
        count2 = 0

        for i in range(len(nums)):
            if nums[i] == majority:
                count += 1
            elif nums[i] == majority2:
                count2 += 1
            elif count == 0:
                majority = nums[i]
                count += 1
            elif count2 == 0:
                majority2 = nums[i]
                count2 += 1
            elif (nums[i] != majority) and (nums[i] != majority2):
                count -= 1
                count2 -= 1
        
        res = []
        if nums.count(majority) > (len(nums) / 3):
            res.append(majority)
        if nums.count(majority2) > (len(nums) / 3) and (majority2 != majority):
            res.append(majority2)
        return res
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        maxCount = 0
        res = 0
        for num in nums:
            if num in count:
                count[num] += 1
            if num not in count:
                count[num] = 1
            if count[num] > maxCount:
                res = num
                maxCount = max(maxCount, count[num])
        return res
        
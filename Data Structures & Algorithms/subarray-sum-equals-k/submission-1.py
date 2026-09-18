class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        sumCounts = {0 : 1}
        res = 0
        for n in nums:
            curSum += n
            diff = curSum - k
            if diff in sumCounts:
                res += sumCounts[diff]
            if curSum in sumCounts:
                sumCounts[curSum] += 1
            else:
                sumCounts[curSum] = 1
        return res
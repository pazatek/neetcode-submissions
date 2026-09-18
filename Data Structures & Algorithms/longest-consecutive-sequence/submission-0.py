class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxSequenceLength = 0
        for num in s:
            sequenceLength = 0
            if num - 1 in s:
                continue
            while num in s:
                sequenceLength += 1
                num += 1
            if sequenceLength > maxSequenceLength:
                maxSequenceLength = sequenceLength
        return maxSequenceLength

                

        
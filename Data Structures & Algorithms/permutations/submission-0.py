class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def permsFrom(i):
            if i == len(nums):
                return [[]]

            permsWithoutCurr = permsFrom(i + 1)

            result = []
            for permWithoutCurr in permsWithoutCurr:
                for insertPos in range(len(permWithoutCurr) + 1):
                    newPerm = permWithoutCurr.copy()
                    newPerm.insert(insertPos, nums[i])
                    result.append(newPerm)
            return result

        return permsFrom(0)
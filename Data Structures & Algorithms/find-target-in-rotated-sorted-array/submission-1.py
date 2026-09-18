class Solution:
    def search(self, nums: List[int], target: int) -> int:
        leftIndex = 0
        rightIndex = len(nums) - 1
        while leftIndex < rightIndex:
            middleIndex = (leftIndex + rightIndex) // 2
            if (nums[middleIndex] < nums[rightIndex]):
                rightIndex = middleIndex
            else:
                leftIndex = middleIndex + 1
        pivotIndex = leftIndex
        if nums[pivotIndex] <= target <= nums[-1]:
            leftIndex = pivotIndex
            rightIndex = len(nums) - 1
        else:
            leftIndex = 0
            rightIndex = pivotIndex - 1
        while leftIndex <= rightIndex:
            middleIndex = (leftIndex+rightIndex) // 2
            if nums[middleIndex] == target:
                return middleIndex
            elif nums[middleIndex] < target:
                leftIndex = middleIndex + 1
            elif nums[middleIndex] > target:
                rightIndex = middleIndex - 1
        return -1
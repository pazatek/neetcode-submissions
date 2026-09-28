class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1:  1     3 |          8
        # nums2:     2    | 4  5        9
        if len(nums1) > len(nums2):
            temp = nums2
            nums2 = nums1
            nums1 = temp
        perHalf = (len(nums1) + len(nums2)) // 2
        left = 0
        right = len(nums1)
        while right >= left:
            iCut = (right + left) // 2
            jCut = perHalf - iCut

            if iCut - 1 >= 0:
                nums1LeftEnd = nums1[iCut - 1]
            else:
                nums1LeftEnd = float('-inf')

            if iCut < len(nums1):
                nums1RightStart = nums1[iCut]
            else:
                nums1RightStart = float('inf')
            
            if jCut - 1 >= 0:
                nums2LeftEnd = nums2[jCut - 1]
            else:
                nums2LeftEnd = float('-inf')

            if jCut < len(nums2):
                nums2RightStart = nums2[jCut]
            else:
                nums2RightStart = float('inf')

            if (nums1LeftEnd <= nums2RightStart) and (nums2LeftEnd <= nums1RightStart):
                totalSize = len(nums1) + len(nums2)
                if totalSize % 2 == 0:
                    return (min(nums1RightStart, nums2RightStart) + max(nums1LeftEnd, nums2LeftEnd)) / 2
                else:
                    return min(nums1RightStart, nums2RightStart) 
            elif (nums1LeftEnd > nums2RightStart):
                right = iCut - 1
            else:
                left = iCut + 1




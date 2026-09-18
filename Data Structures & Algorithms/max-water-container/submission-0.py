class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        currentWater = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            height = min(heights[l],heights[r])
            width = r - l
            currentWater = height * width

            maxWater = max(currentWater, maxWater)

            if heights[l] < heights[r]:
                l += 1
            elif heights[l] >= heights[r]:
                r -= 1
        return maxWater





        
class Solution:
    def trap(self, height: List[int]) -> int:
        rightMax = [0] * len(height)
        leftMax = [0] * len(height)
        for i in range(len(height)):
            if i == 0:
                leftMax[0] = height[0]
                continue
            leftMax[i] = max(leftMax[i - 1], height[i])
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                rightMax[-1] = height[-1]
                continue
            rightMax[i] = max(rightMax[i + 1], height[i])
        res = 0
        for i in range(len(height)):
            res += min(leftMax[i],rightMax[i]) - height[i]
        return res
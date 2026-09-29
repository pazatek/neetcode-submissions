class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i, newheight in enumerate(heights):
            start = i
            while stack and stack[-1][1] > newheight:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                start = index 
            stack.append((start, newheight))
        for i, height in stack:
            maxArea = max(maxArea, height * (len(heights) - i))
        return maxArea
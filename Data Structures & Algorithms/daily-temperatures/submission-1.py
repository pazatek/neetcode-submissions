class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i, newtemp in enumerate(temperatures):
            while stack and stack[-1][1] < temperatures[i]:
                day, temp = stack.pop()
                result[day] = i - day
            stack.append((i, newtemp))
        return result
                
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index, temperature in enumerate(temperatures):
            while stack and stack[-1][0] < temperature:
                stack_temp, stack_index = stack.pop()
                result[stack_index] = index - stack_index
            stack.append((temperature, index))
        return result

        

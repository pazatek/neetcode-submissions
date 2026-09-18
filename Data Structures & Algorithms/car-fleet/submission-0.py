class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = []
        stack = []
        for i in range(len(position)):
            pairs.append([position[i],speed[i]])
        pairs.sort()
        for i in range(len(pairs) - 1, -1, -1):
            timeToArrive = (target - pairs[i][0]) / pairs[i][1]
            if not stack:
                stack.append(timeToArrive)
            elif timeToArrive > stack[-1]:
                stack.append(timeToArrive)
        return len(stack)
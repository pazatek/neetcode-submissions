class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = 0
        start = 0
        travelled = 0
        for i in range(len(gas)):
            tank += gas[i]
            tank -= cost[i]
            travelled += (gas[i] - cost[i])
            if tank < 0:
                start = i + 1
                tank = 0
        return start if travelled >= 0 else -1

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        start = 0
        tank = 0
        for i in range(len(gas)):
            tank += (gas[i] - cost[i])
            # can't reach next station with current tank balance
            # so we restart at the next one
            if tank < 0:
                start = i + 1
                tank = 0
        return start

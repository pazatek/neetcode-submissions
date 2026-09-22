class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(index):
            if index in memo:
                return memo[index]
            # if you jumped out of cost, you're done
            if index >= len(cost):
                return 0
            # wherever you just jumped to, add it to cost
            memo[index] = cost[index] + min(dp(index + 1), dp(index + 2))
            return memo[index]
        return min(dp(0), dp(1))

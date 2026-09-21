class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')
            best = float('inf')
            for coin in coins:
                best = min(best, 1 + dfs(remaining - coin))
            memo[remaining] = best
            return best
        best = dfs(amount)
        return -1 if best == float('inf') else best
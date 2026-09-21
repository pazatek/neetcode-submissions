class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]
            best = float('inf')
            for c in coins:
                best = min(1 + dfs(amount - c), best)
            memo[amount] = best
            return best

        return -1 if dfs(amount) == float('inf') else dfs(amount)

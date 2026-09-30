class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [-1] * (amount + 1)
        minCoins = 0
        def dfs(amount):
            if amount == 0:
                return 0
            if memo[amount] != -1:
                return memo[amount]
            minCoins = float("inf")
            for c in coins:
                if (amount - c) >= 0:
                    minCoins = min(minCoins, dfs(amount - c) + 1)
            memo[amount] = minCoins
            return minCoins

        minCoins = dfs(amount)
        if minCoins == float("inf"):
            return -1
        else:
            return minCoins

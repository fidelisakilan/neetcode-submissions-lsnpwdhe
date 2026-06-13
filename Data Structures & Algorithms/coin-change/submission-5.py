class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(value):
            if value == 0:
                return 0
            if value < 0:
                return float("inf")
            if value in memo:
                return memo[value]
            minCoins = float("inf")
            for coin in coins:
                minCoins = min(minCoins, dfs(value - coin) + 1)
            memo[value] = minCoins
            return minCoins

        

        res = dfs(amount)
        if res == float("inf"):
            return -1
        return res



        

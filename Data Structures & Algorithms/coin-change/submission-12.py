class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount in memo:
                return memo[amount]
            res = float("inf")
            for c in coins:
                res = min(res, 1 + dfs(amount - c))
            memo[amount] = res
            return res
        
        res = dfs(amount)
        if res != float("inf"): return res
        else: return -1
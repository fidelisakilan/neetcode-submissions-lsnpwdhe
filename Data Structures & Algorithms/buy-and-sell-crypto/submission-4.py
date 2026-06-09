class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        res = 0

        l = 0 
        r = 1

        while l < r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = r + 1
                continue
            res = max(res, prices[r] - prices[l])
            r += 1
        return res
            

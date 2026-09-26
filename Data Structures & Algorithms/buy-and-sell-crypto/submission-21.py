class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        maxRes = 0
        l, r = 0, 1
        while l < r and r < len(prices):
            if prices[l] > prices[r]:
                l = r
            print(l, r, prices[l], prices[r])
            maxRes = max(maxRes, prices[r] - prices[l])
            r += 1
        return maxRes
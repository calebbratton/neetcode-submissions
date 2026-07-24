class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        minBuy = prices[0]

        for p in prices:
            profit = p - minBuy
            res = max(profit, res)
            minBuy = min(p, minBuy)

        return res
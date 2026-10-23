class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        bestSell = 0
        for p in prices:
            bestBuy = min(bestBuy, p)
            bestSell = max(bestSell, p - bestBuy)
        return bestSell

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        n = len(prices)

        for i in range(1,n):
            gain = prices[i] - prices[i-1]

            if gain > 0:
                profit += gain
        
        return profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mini = prices[0]
        ans = 0

        for price in prices:
            mini = min(mini,price)
            profit = price - mini

            ans = max(ans,profit)
        
        return ans 
            
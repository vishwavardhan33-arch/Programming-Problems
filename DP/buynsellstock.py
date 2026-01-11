class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        n = len(prices)
        maxi = float('-inf')
        for sell in range(1,n):
            if prices[sell]<prices[buy]:
                buy = sell
            else:
                curr = prices[sell]-prices[buy]
                maxi = max(maxi,curr)
        if maxi == float('-inf'):
            return 0
        return maxi

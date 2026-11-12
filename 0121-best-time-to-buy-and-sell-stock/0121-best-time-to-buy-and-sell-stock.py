class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit=0
        mi=prices[0]
        for i in range(1,len(prices)):
            if mi>prices[i]:
                mi=prices[i]
            profit=max(profit,abs(prices[i]-mi))
            print(profit)
        return profit
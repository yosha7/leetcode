class Solution(object):
    def maxProfit(self, prices):
        maxprofit=0
        minprice=prices[0]
        i=0
        while i<len(prices):
           minprice=min(minprice,prices[i])
           profit=prices[i]-minprice
           maxprofit=max(maxprofit,profit)
           i+=1
        return maxprofit
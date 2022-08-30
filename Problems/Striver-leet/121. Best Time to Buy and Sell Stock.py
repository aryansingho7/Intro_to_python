class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cp,sp=0,1
        maxprofit=0
        
        while sp<len(prices):
            if prices[cp]<prices[sp]:
                profit=prices[sp]-prices[cp]
                maxprofit=max(maxprofit, profit)
            else:
                cp=sp
            sp+=1
        return maxprofit
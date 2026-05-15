class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buy=prices[0]
        # maxprofit=0
        # for i in prices[1:]:
        #     if i<buy:
        #         buy=i+fee
        #     maxprofit=max(maxprofit,i-buy)
        # return maxprofit


        
        buy=prices[0]
        maxprofit=0
        for i in prices[1:]:
            if i<buy:
                buy=i
            elif i>buy+fee:
                maxprofit+=i-buy-fee
                buy=i-fee
            # maxprofit=max(maxprofit,i-buy)
        return maxprofit









        buy=prices[0]
        maxprofit=0
        for i in prices[1:]:
            if i<buy:
                buy=i
            elif prices[i]>buy+fee:
                maxprofit+=prices[i]-buy-fee
                buy=prices[i]-fee
        return maxprofit
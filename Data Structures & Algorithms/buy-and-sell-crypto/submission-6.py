class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price = 0

        l, r = 0, 0

        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                max_price = max(max_price, price)
            else:
                l = r
            
            r+=1
        
        return max_price


















            






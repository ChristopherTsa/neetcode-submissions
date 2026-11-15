class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        out = 0
        n = len(prices)

        left = 0
        right = 1

        while left < n and right < n:
            l = prices[left]
            r = prices[right]
            profit = r - l
            
            out = max(profit, out)
                
            if profit < 0:
                left = right
            
            right +=1
        
        return out
                



        
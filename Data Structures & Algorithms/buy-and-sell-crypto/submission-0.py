class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPro = 0
        for i in range(len(prices)):
            last = len(prices)-1
            while last > i:
                if prices[last] - prices[i] > maxPro:
                    maxPro = prices[last] - prices[i]
                
                last -= 1   

        return maxPro
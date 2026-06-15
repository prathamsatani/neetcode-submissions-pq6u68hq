class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        currMin = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
            
            if prices[i] - currMin > maxDiff:
                maxDiff = prices[i] - currMin
            
        return maxDiff
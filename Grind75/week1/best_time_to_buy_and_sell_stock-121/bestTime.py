from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currProfit = 0
        lowest = prices[0]
        for p in prices:
            if p < lowest: 
                lowest = p
            tmp = p - lowest 
            if tmp > currProfit:
                currProfit = tmp 
        return currProfit


s = Solution()

prices = [7,1,5,3,6,4]
expected = 5

assert s.maxProfit(prices) == expected



    
class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_price = 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p > min_price:
                t = p - min_price
                max_price = max(t, max_price)
        return max_price
        






sol = Solution()

t1 = [7,1,5,3,6,4]
s1 = 5
t2 = [7,6,4,3,1]
s2 = 0

print(sol.maxProfit(t1))
print(sol.maxProfit(t2))
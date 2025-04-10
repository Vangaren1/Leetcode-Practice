class Solution:
    results = {1:True, 2:True}
    def canWinNim(self, n):
        if n == 1 or n == 2:
            return True
        if n < 1: 
            return False
        if n in self.results.keys():
            return self.results[n]
        else:
            self.results[n] = not (self.canWinNim(n-1) and self.canWinNim(n-2) and self.canWinNim(n-3)) 
        #print(n, m1,m2,m3)
        return self.results[n]

sol = Solution()
print(sol.canWinNim(100))
from typing import Optional, List


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        coins = []
        
        for index in range(len(numWays)):
            if numWays[index] == 0:
                continue
            if numWays[index] == 1:
                coins.insert(0,index+1)
                continue
            
            value = index + 1
            for coin in coins:
                value = value % coin
                if value == 0:
                    break
            if value == 0:
                coins.insert(0, index+1)
        
        return coins

if __name__ == "__main__":
    numWays = [0,1,0,2,0,3,0,4,0,5]
    out = [2,4,6]
    s = Solution()
    print(s.findCoins(numWays))
    print("Running Solution...")

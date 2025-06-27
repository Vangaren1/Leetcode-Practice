from typing import Optional, List, Tuple
from functools import lru_cache
from itertools import combinations

class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        coins = []

        for index in range(len(numWays)):
            target = index + 1

            combCount = self.countCombinations_cached(target, tuple(sorted(coins)))
            diff = numWays[index] - combCount

            if diff == 1:
                coins.append(target)
            elif diff != 0:
                return []

        return coins

    @lru_cache(maxsize=None)
    def countCombinations_cached(self, target: int, coins: Tuple[int]) -> int:
        if target == 0:
            return 1
        if target < 0 or not coins:
            return 0

        total = 0
        for i, coin in enumerate(coins):
            if coin > target:
                break
            total += self.countCombinations_cached(target - coin, coins[i:])  # avoid permutations
        return total

        
        


if __name__ == "__main__":
    numWays = [1,1,2,3,4,6,7,9,12,15,18,23,27,32,39,46,53,63,72,83,96,109,123,141,158,177,199,222,246,275,303,334,369,405,443,487,530,577,629,683,739,802,865,933,1007,1083,1162,1250,1338,1432,1533,1637,1745,1863,1982,2108,2242,2380,2523,2678,2834,2998,3172,3351,3536,3734,3934,4144,4365,4592,4826,5075,5327,5590,5866,6149,6440,6748,7060,7385,7724,8071,8428,8804,9185,9580,9991,10412,10844,11297,11756,12231,12724,13228,13745,14285]
    out = [2,4,6]
    s = Solution()
    
    coins = [2,4]
    target = 6
    
    # print(s.countAllCombinations(target, coins))
    
    print(s.findCoins(numWays))
    print("Running Solution...")




        # coins = []
        
        # for index in range(len(numWays)):
        #     if numWays[index] == 0:
        #         continue
        #     if numWays[index] == 1:
        #         coins.insert(0,index+1)
        #         continue
            
        #     value = index + 1
        #     for coin in coins:
        #         value = value % coin
        #         if value == 0:
        #             break
        #     if value == 0:
        #         coins.insert(0, index+1)
        
        # return coins
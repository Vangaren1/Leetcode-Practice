from typing import Optional, List

from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        seen = set()
        
        for first in range(len(nums)-1):
            second = first + 1
            third = len(nums) - 1
            
            while second < third:
                fnum = nums[first]
                snum = nums[second]
                tnum = nums[third]
                if fnum + snum + tnum < 0:
                    second += 1
                elif fnum + snum + tnum > 0:
                    third -= 1
                else: 
                    tmp = (fnum, snum, tnum)
                    if tmp not in seen:
                        seen.add(tmp)
                        results.append([ t for t in tmp ])
                    else:
                        second += 1
        return results
        

if __name__ == "__main__":
    nums = [-1,0,1,2,-1,-4]
    expected = [[-1,-1,2],[-1,0,1]]
    
    s = Solution()
    
    print(s.threeSum(nums))
    
    print("Running Solution...")

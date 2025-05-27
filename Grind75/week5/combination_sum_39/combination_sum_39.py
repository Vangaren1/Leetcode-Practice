from typing import Optional, List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        found = set()
        
        def treeFind(curr, nums, target):
            if target < 0:
                return 
            if target == 0:
                curr.sort()
                found.add(tuple(curr))
            else:
                for n in nums:
                    if (target - n) >= 0:
                        treeFind(curr + [n], nums, target - n)
        treeFind([], candidates, target)

        rVal = [ list(t) for t in found ]

        return rVal
        
        
if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    s = Solution()
    
    print(s.combinationSum( candidates, target))
    print("Running Solution...")

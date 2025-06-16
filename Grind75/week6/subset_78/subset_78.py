from typing import Optional, List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        curr = []
        def dfs(i):
            if i >= len(nums):
                res.append(curr.copy())
                return 
            
            # inclued i in subset
            curr.append(nums[i])
            dfs(i+1)
            
            # do not include i
            curr.pop()
            dfs(i+1)
        
        dfs(0)
        return res


if __name__ == "__main__":
    
    s = Solution()
    nums = [1,2, 3]
    print(s.subsets(nums))
    print("Running Solution...")

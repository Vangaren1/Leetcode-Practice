from typing import Optional


class Solution:
    def climbStairs(self, n: int) -> int:
        steps = {1:1, 2:2}
        def climbRec(n):
            if n in steps:
                return steps[n]
            steps[n] = climbRec(n-1) + climbRec(n-2)
            return steps[n]
        return climbRec(n)
            
        
        pass 
if __name__ == "__main__":
    s = Solution()
    for n in range(1,10):
        print(s.climbStairs(n))
    print("Running Solution...")

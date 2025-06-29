from typing import Optional, List


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left = 1
        right = x // 2

        mid = (left + right ) //2 
        while left <= right:
            curr = mid * mid 
            cnext = (mid + 1) * (mid + 1)
            if curr == x:
                return mid
            
            if curr < x and cnext > x:
                return mid

            if curr > x: 
                right = mid -1
            else:
                left  = mid + 1
            mid = (left + right) // 2
        return mid

if __name__ == "__main__":
    x = 2147395599
    s = Solution()
    print(s.mySqrt(x))
    print("Running Solution...")

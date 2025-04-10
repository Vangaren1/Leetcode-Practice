class Solution:
    def isHappy(self, n: int) -> bool:
        def proc(n):
            s = str(n)
            total = 0
            for c in s:
                total += (int(c) ** 2)
            return total
        seen = {n}
        temp = n
        seen.add(temp)
        while True:
            temp = proc(temp)
            if temp == 1:
                return True
            if temp in seen:
                return False
            seen.add(temp)



obj=Solution()

print(obj.isHappy(2))
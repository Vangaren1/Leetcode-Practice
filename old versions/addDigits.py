class Solution:
    def addDigits(self, num: int) -> int:
        sNum = str(num)
        while len(sNum) > 1:
            tsum = 0
            for i in sNum:
                tsum += int(i)
            sNum = str(tsum)
        return int(sNum)

obj = Solution()
print(obj.addDigits("173"))
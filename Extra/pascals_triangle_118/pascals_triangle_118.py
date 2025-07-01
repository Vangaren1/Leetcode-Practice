from typing import Optional, List


class Solution:
    
    def generate(self, numRows: int) -> List[List[int]]:
        baseCase = [[1], [1,1]]
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return baseCase
        tmp = self.generate(numRows-1)
        lastRow = tmp[-1]
        newRow = [1,]
        for index in range(len(lastRow)-1):
            newNum = lastRow[index] + lastRow[index+1]
            newRow.append(newNum)
        newRow.append(1)
        tmp.append(newRow)
        return tmp

if __name__ == "__main__":
    s = Solution()
    for i in range(5):
        print(s.generate(i))
    print("Running Solution...")

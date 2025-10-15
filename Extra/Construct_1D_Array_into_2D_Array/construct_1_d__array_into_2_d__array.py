from typing import Optional, List


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        count = m * n
        result = []
        if len(original) > count:
            return result

        for row in range(m):
            start = 0 + n * row
            end = n + n * row
            tmp = original[start:end]
            result.append(tmp)
        return result


if __name__ == "__main__":
    sol = Solution()
    original = [1, 2, 3]
    m = 1
    n = 3
    r = sol.construct2DArray(original, m, n)
    for row in r:
        print(row)
    print("Running Solution...")

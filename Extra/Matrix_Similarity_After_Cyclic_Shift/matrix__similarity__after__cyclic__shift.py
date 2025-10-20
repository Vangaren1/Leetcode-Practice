from typing import Optional, List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def check(old, mod):
            for index in range(len(old)):
                if old[index] != mod[index]:
                    return False
            return True

        for index in range(len(mat)):
            tmp = mat[index].copy()
            if index % 2 == 0:
                for s in range(k):
                    tmp.append(tmp.pop(0))
            else:
                for s in range(k):
                    tmp.insert(0, tmp.pop())
            if not check(tmp, mat[index]):
                return False

        return True


if __name__ == "__main__":
    sol = Solution()
    mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    k = 4
    print(sol.areSimilar(mat, k))
    print("Running Solution...")

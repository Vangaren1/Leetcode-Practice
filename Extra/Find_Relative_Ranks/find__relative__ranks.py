from typing import Optional, List
import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)

        results = [None] * n

        q = []
        for index in range(n):
            heapq.heappush(q, (score[index], index))

        while q:
            qSize = len(q)
            score, idx = heapq.heappop(q)

            if qSize > 3:
                results[idx] = str(qSize)
            elif qSize == 3:
                results[idx] = "Bronze Medal"
            elif qSize == 2:
                results[idx] = "Silver Medal"
            elif qSize == 1:
                results[idx] = "Gold Medal"
        return results


if __name__ == "__main__":
    sol = Solution()
    score = [10, 3, 8, 9, 4]
    print(sol.findRelativeRanks(score))
    print("Running Solution...")

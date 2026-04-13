from typing import Optional, List
import heapq, csv, ast, math
from collections import defaultdict
from pathlib import Path


# queries[i] = [li, ri, ki, vi].
class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        qdict = defaultdict(list)
        bucketSize = defaultdict(lambda: 0)
        MOD = 10**9 + 7
        n = len(nums)
        B = int(math.sqrt(n))
        for q in queries:
            l, r, k, v = q
            if k > B:
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % (10**9 + 7)
            else:
                tmp = (k, l % k)
                qdict[tmp].append(q)
                size = ((n - 1 - r) // k) + 1
                bucketSize[tmp] = max(bucketSize[tmp], size)

        for (k, rem), group in qdict.items():
            bucket_len = ((n - 1 - rem) // k) + 1
            bucket = [1] * (bucket_len + 1)

            for l, r, _, v in group:
                start = (l - rem) // k
                end = (r - rem) // k

                bucket[start] = (bucket[start] * v) % MOD

                if end + 1 < len(bucket):
                    bucket[end + 1] = (bucket[end + 1] * pow(v, MOD - 2, MOD)) % MOD

            cur = 1
            for pos in range(bucket_len):
                cur = (cur * bucket[pos]) % MOD
                real_idx = rem + pos * k
                nums[real_idx] = (nums[real_idx] * cur) % MOD

        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = []
    numFile = Path(__file__).parent / "nums.csv"
    with open(numFile, newline="") as f:
        rows = csv.reader(f)
        for row in rows:
            for num in row:
                nums.append(int(num))
    qFile = Path(__file__).parent / "queries.txt"
    with open(qFile, "r") as q:
        text = q.read()
    queries = ast.literal_eval(text)

    print(sol.xorAfterQueries(nums, queries))

    print("Running Solution...")

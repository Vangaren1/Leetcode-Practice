from typing import Optional, List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        rem = total % p
        if rem == 0:
            return 0

        n = len(nums)
        curr = 0
        best = n
        seen = {0: -1}  # prefix_mod -> latest index

        for i, x in enumerate(nums):
            curr = (curr + x) % p
            target = (curr - rem) % p
            if target in seen:
                best = min(best, i - seen[target])
            seen[curr] = i

        return best if best < n else -1


if __name__ == "__main__":
    sol = Solution()
    nums = [6, 3, 5, 2]
    p = 9

    # nums = [6, 3, 5, 2]
    # p = 9
    print(sol.minSubarray(nums, p))
    print("Running Solution...")


"""

doesn't work with large arrays 

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        currSum = sum(nums)
        remainder = currSum % p
        if remainder == 0:
            return 0
        if currSum < p:
            return -1

        n = (currSum - remainder) // p
        possibleSums = [i * p + remainder for i in range(n)]
        seen = {0: -1}

        maxLen = float("inf")

        prefix = 0
        for index, num in enumerate(nums):
            prefix += num

            for target in possibleSums:
                need = prefix - target
                if need in seen:
                    start = seen[need] + 1
                    maxLen = min(maxLen, index - start + 1)

            if prefix not in seen:
                seen[prefix] = index
        return maxLen if maxLen != float("inf") else -1



class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        currSum = sum(nums)
        target = currSum % p
        if target == 0:
            return 0
        if currSum < p:
            return -1
        dp = [0]
        for index, num in enumerate(nums):
            dp.append(num + dp[index])

        minLen = float("inf")
        while target < currSum:

            ptr1, ptr2 = 0, 1

            while ptr2 <= len(nums):
                cSum = dp[ptr2] - dp[ptr1]
                if cSum < target:
                    ptr2 += 1
                    continue
                if cSum == target:
                    minLen = min((ptr2 - ptr1), minLen)
                ptr1 += 1
                ptr2 = ptr1 + 1
            target += p
        return minLen if minLen < float("inf") else -1        
        
        """

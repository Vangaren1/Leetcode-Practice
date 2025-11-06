from typing import Optional, List
from collections import Counter
import SortedList
import heapq


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = Counter()
        top = SortedList()
        rest = SortedList()
        top_sum = 0
        ans = []

        def balance():  # keeps top and rest balanced
            nonlocal top_sum
            while len(top) < x and rest:
                f, v = rest.pop()
                top.add((f, v))
                top_sum += f * v
            while len(top) > x:
                f, v = top.pop(0)
                top_sum -= f * v
                rest.add((f, v))
            while rest and top and rest[-1] > top[0]:
                f1, v1 = rest.pop()
                f2, v2 = top.pop(0)
                top_sum += f1 * v1 - f2 * v2
                top.add((f1, v1))
                rest.add((f2, v2))

        def add(num):
            nonlocal top_sum
            old = (freq[num], num)
            if old in top:
                top.remove(old)
                top_sum -= old[0] * old[1]
            elif old in rest:
                rest.remove(old)
            freq[num] += 1
            new = (freq[num], num)
            rest.add(new)
            balance()

        def remove(num):
            nonlocal top_sum
            old = (freq[num], num)
            if old in top:
                top.remove(old)
                top_sum -= old[0] * old[1]
            else:
                rest.remove(old)
            freq[num] -= 1
            if freq[num] > 0:
                rest.add((freq[num], num))
            else:
                del freq[num]
            balance()

        for i in range(k):  # initial window
            add(nums[i])
        ans.append(top_sum)

        for i in range(k, len(nums)):  # slide the window
            remove(nums[i - k])
            add(nums[i])
            ans.append(top_sum)

        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 1, 2, 2, 3, 4, 2, 3]
    k = 6
    x = 2
    print(sol.findXSum(nums, k, x))
    expected = [11, 15, 15, 15, 12]
    print("Running Solution...")


"""
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        count = Counter()
        heap = []
        heapSet = set()


        def push(val):
            count[val] += 1
            if val not in heapSet:
                heapSet.add(val)
                heapq.heappush(heap, (-count[val], val))
            

        def pop(val):
            curr = count[val] - 1
            if curr <= 0:
                del count[val]
            else:
                count[val] = curr
                heapq.heappush(heap, (-curr, val))

        def topValid():
            tmp = []
            valid = []
            isValid = set()
            while heap and len(isValid) < x:
                currNeg, val = heapq.heappop(heap)
                curr = count[val]
                if curr == -currNeg and val not in isValid:
                    isValid.add(val)
                    valid.append((curr, val))
                    tmp.append((currNeg, val))

            for item in tmp:
                heapq.heappush(heap, item)

            valid.sort(reverse=True)
            return valid

        def calcWindow():
            total = 0
            c = 0
            vals = topValid()
            for cnt, val in vals:
                c += 1
                if c <= x:
                    total += cnt * val
            return total

        for val in nums[:k]:
            push(val)

        output = []
        output.append(calcWindow())

        for i in range(k, len(nums)):
            push(nums[i])
            pop(nums[i - k])
            output.append(calcWindow())

        return output        
        
        
        """

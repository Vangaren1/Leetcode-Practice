from typing import Optional, List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [numbers[left], numbers[right]]
            elif total < target:
                left += 1
            else:
                right -= 1

        return None
        pass


if __name__ == "__main__":
    sol = Solution()
    print("Running Solution...")

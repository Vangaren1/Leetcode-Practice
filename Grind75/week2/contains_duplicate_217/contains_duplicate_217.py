from typing import Optional, List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

if __name__ == "__main__":
    print("Running Solution...")

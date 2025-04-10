class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for i in nums:
            if i in seen:
                return False
            else:
                seen[i]=True
        return True
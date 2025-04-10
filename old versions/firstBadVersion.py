# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version == bad 


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        left = 1
        right = n 
        mid = (left + right) // 2
        checkM = isBadVersion(mid)
        checkMM = isBadVersion(mid - 1)
        while not (checkM and not checkMM):
            # print("checking left: %d, mid: %d, right: %d, checkM: %s checkMM: %s" % (left,mid, right, str(checkM), str(checkMM)))
            if checkM:
                right = mid
                mid = (left + right) // 2 
            else:
                left = mid + 1
                mid = (left + right) // 2
            checkM = isBadVersion(mid)
            checkMM = isBadVersion(mid - 1)
        return mid


obj = Solution()
#bad = 1702766719
bad = 2

# print(obj.firstBadVersion(2126753390))
print(obj.firstBadVersion(4))
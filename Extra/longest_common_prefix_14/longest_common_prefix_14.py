from typing import Optional, List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 1:
            return strs[0]
        # this is the max length ihe prefix can be
        length = min( [ len(s) for s in strs])
        for index in range(length):
            tmp = strs[0][index]
            for s in strs:
                if s[index] != tmp:
                    prefix = s[:index]
                    return prefix
            prefix = s[:index+1]
        return prefix

if __name__ == "__main__":
    strs = ["dog","racecar","car"]
    # strs = ["a","ab"]
    strs = ["flower","flow","flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
    print("Running Solution...")

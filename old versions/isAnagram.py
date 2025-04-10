class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def buildDict(r):
            d = {}
            for c in r:
                if c in d:
                    d[c] += 1
                else:
                    d[c] = 1
            return d
        sDict = buildDict(s)
        tDict = buildDict(t)
        for tC in tDict:
            if tC in sDict:
                if tDict[tC] != sDict[tC]:
                    return False
            else:
                return False
        for sC in sDict:
            if sC in tDict:
                if tDict[sC] != sDict[sC]:
                    return False
            else:
                return False
        return True

        


obj = Solution()

s = "anagram"
t = "nagaram"

print(obj.isAnagram(s,t))

s = "rat"
t = "car"

print(obj.isAnagram(s,t))
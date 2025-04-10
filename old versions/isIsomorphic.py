class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def build(str1):
            iso = {}
            count = 0
            l = []
            for c in str1:
                if c in iso:
                    l.append(iso[c])
                else:
                    iso[c] = count
                    l.append(count)
                    count += 1
            return l
        if len(s) != len(t):
            return False
        iso_s = build(s)
        iso_t = build(t)
        for i in range(len(s)):
            if iso_s[i] != iso_t[i]:
                return False
        return True





obj = Solution()
print(obj.isIsomorphic('aba', 'chc'))
class Solution:
    def wordPattern(self, pattern, s):
        d = {}
        w = s.split()
        if len(pattern) != len(w):
            return False
        for i in range(len(pattern)):
            key = pattern[i]
            word = w[i]
            print("checking key: %s, word: %s, i: %d", (key,word,i))
            if word in d.values():
                if key not in d:
                    return False
                if d[key] != word:
                    return False
            else:
                if key in d:
                    return False
                d[key] = word
        return True


sol = Solution()

pattern = "abba"
st = "dog cat cat dog"

print(sol.wordPattern(pattern, st))

        
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''.join([ i for i in s if i.isalpha()])
        new_s = new_s.lower()
        l_s = len(new_s)
        if l_s in [0,1]:
            return True
        if new_s[0] != new_s[-1]:
            return False
        while len(new_s) > 1 :
            if self.endsMatch(new_s):
                return False
            new_s = new_s[1:-1]
        return True
    def endsMatch(self, s: str) -> bool:
        return s[0] != s[-1]

s = Solution()
cases = ['    ', 'a q234   ab aa', 'aaa', 'abc', "A man, a plan, a canal: Panama", "0P" ]
for c in cases:
    print(s.isPalindrome(c))
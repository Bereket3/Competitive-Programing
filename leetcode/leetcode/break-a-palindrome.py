class Solution:
    def breakPalindrome(self, p: str) -> str:
        if len(p) <= 1:return ''
        n = p.__len__()

        for i in range(len(p)):
            if n%2 != 0 and i == n//2:
                continue
            elif p[i] != 'a':
                return p[:i] + 'a' + p[i+1:]
            elif p[i] == 'a' and i == n - 1:
                return p[:-1] + 'b'
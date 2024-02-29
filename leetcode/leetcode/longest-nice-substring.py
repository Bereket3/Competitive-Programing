class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def help(st, en):
            t = set(s[st:en])
            for i in t:
                if (i.lower() in t) != (i.upper() in t):
                    return False
            return True


        best = ''
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if help(i, j) and len(best) < s[i:j].__len__():
                    best = s[i:j]

        return best

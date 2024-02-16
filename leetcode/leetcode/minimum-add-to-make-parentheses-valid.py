class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        if not s:return 0
       
        opens = 0
        res = 0
        for i in s:
            if i == '(':
                opens += 1
            else:
                if opens <= 0:
                    res += 1
                else:
                    opens -= 1
        return res + opens

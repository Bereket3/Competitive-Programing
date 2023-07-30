class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res,last_index = "",0
        for i in spaces:
            res += s[last_index:i]
            res += " "
            last_index = i
        res += s[last_index:]
        return(res)

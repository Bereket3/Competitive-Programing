class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        out = 0
        for i in range(len(s)-1):
            if mapper[s[i]] <  mapper[s[(i+1)]]:
                out-= mapper[s[i]]
            else:
                out+= mapper[s[i]]

        return out+ mapper[s[-1]]
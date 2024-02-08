class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        modifide = [0]*(len(s) + 1)
    
        for start, end, directions in shifts:
            modifide[start] += directions if directions else -1
            modifide[end + 1] -= directions if directions else -1

        out = []
        for i in range(len(s)):
            if i != 0: 
                modifide[i] += modifide[i - 1]
            new = (ord(s[i]) - ord("a") + modifide[i]) % 26 + ord("a")
            out.append(chr(new))


        return ''.join(out)
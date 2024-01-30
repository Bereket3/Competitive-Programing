class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        out_put: int = 0
        current: int = 0
        vowles: str = 'aeiou'
        for i in range(k):
            if s[i] in vowles:
                current += 1
        out_put = current
        
        for i in range( k, s.__len__()):
            if s[i] in vowles:
                current += 1
            if s[i - k] in vowles:
                current -= 1
            out_put = max(current, out_put)

        return out_put

       
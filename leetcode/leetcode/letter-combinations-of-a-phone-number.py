class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0: return []

        digit_to_chars = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        out = ['']

        for d in digits:
            letters = digit_to_chars[int(d) - 2]
            out = [prefix + letter for prefix in out for letter in letters]

        return out

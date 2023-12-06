class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = [0] * len(indices)
        for idx, letter in zip(indices, s):
            answer[idx] = letter
        return ''.join(answer)
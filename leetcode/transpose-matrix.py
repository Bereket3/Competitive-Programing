class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        out = []
        for i in zip(*matrix):
            out.append(list(i))

        return out
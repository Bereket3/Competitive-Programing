class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        out = 0
        for i in range(mat.__len__()):
            out += mat[i][i]
            out += mat[i][len(mat) - i -1]

        return out - mat[len(mat)//2][len(mat)//2] if len(mat) %2 != 0 else out
        
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for j, i in enumerate(zip(*matrix)):
            matrix[j] = list(i[::-1])
class NumMatrix:

    def __init__(self, a: List[List[int]]):
        self.mat = a
        pri = [[0]*(len(a[0]) + 1) for _ in range(len(a)+1)]

        for i in range(1, len(a) + 1):
            for j in range(1, len(a[0]) + 1):
                pri[i][j] =  pri[i - 1][j] + pri[i][j - 1] - pri[i - 1][j - 1] + a[i - 1][j - 1]
                # p[r][c] = p[r-1][c] + p[r][c-1] - p[r-1][c-1] + matrix[r-1][c-1]
        self.pri = pri


    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        return self.pri[r2+1][c2+1] - self.pri[r1][c2+1] - self.pri[r2+1][c1] + self.pri[r1][c1]

        

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
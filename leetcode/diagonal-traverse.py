class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        my_contaner = defaultdict(list)
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                my_contaner[row+col] += [mat[row][col]]

        ans = []
        for i, value in enumerate(my_contaner.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        return ans

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        walk = 0
        for i in range(1, points.__len__()):
            one = abs(points[i][0] - points[i - 1][0])
            two = abs(points[i][1] - points[i-1][1])
            walk += max(one, two)

        return walk
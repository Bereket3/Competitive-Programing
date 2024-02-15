class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort( key = lambda x: x[1])
        tot = 0
        curr = float('-inf')

        for start, end in points:
            if start > curr:
                curr = end
                tot += 1

        return tot
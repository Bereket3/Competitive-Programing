class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        tot = 0
        while target > 1:
            if not maxDoubles:
                return tot + target - 1
                
            if target % 2:
                target -= 1
                tot += 1
            else:
                target //= 2
                maxDoubles -= 1
                tot += 1

        return tot 
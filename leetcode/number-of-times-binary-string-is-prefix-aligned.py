class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        the_max = 0
        count = 0
        for i, j in enumerate(flips):
            the_max = max(the_max, j)
            if the_max <= i+1:
                count +=1

        return count
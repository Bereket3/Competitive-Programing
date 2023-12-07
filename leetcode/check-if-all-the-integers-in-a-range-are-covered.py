class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        the_set = []
        for i in ranges:
          the_set+= [*range(i[0], i[1]+1)]
        the_com = [*range(left, right+1)]
        for i in the_com:
          if i not in the_set:
            return False

        return True
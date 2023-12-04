class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        out = []
        maximum = max(candies)
        for i in range(len(candies)):
            if extraCandies + candies[i] >= maximum:
                out.append(True)
            else:
                out.append(False)

        return out

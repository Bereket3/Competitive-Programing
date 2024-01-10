class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        out = 0
        summed = 0
        for i, j in enumerate(costs):
            summed += j
            if summed > coins:
                return i
            else:
                out = i

        return out + 1
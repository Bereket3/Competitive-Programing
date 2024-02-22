class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost = 0
        diff = []
        for a, b in costs:
            cost += b
            diff.append(a-b)
        diff.sort()
        n = len(costs) // 2
        for i in range(n):
            cost += diff[i]
        return cost
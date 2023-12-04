class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination < start:
            sum1 = sum(distance[destination:start])
            sum2 = sum(distance[:destination]) + sum(distance[start:])
        else:
            sum1 = sum(distance[start:destination])
            sum2 = sum(distance[destination:])  + sum(distance[:start])
        return sum1 if sum1 < sum2 else sum2
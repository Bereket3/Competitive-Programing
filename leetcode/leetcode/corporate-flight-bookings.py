class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        new = [0]*(n + 1)

        for i, j, k in bookings:
            new[i  - 1] += k
            new[j] -= k
        
        for j in range(1, n + 1):
            new[j] += new[j - 1]
            
        new.pop()
        return new

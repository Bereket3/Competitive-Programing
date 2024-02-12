class Solution:
    def carPooling(self, trips, capacity: int) -> bool:  
        pri = [0]*10001
        left = float('inf')
        right = 0
        contaner = 0
        for p, f, t in trips:
            pri[f] += p
            pri[t] -= p
            left = min(left, f)
            right = max(right, t)
        
        for i in range(left, right):
            contaner += pri[i]
            if contaner > capacity:
                return False
            
        return True
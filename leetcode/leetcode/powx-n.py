class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x, n):
            if x==0: return 0
            if n==0: return 1
            return x*helper(x*x, n//2) if n%2 else helper(x*x, n//2)
        return helper(x, abs(n)) if n > 0 else 1/helper(x, abs(n))
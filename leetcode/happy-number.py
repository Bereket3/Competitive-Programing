class Solution:
    def isHappy(self, n: int) -> bool:
        num_set=set()
        while n!=1: 
            n=sum([int(i)**2 for i in str(n)])
            if n in num_set:
                return False
            num_set.add(n)
        return True

        

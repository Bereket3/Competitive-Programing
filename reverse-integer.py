class Solution:
    def reverse(self, x: int) -> int:
        y = abs(x)
        output = []
        the_number = 0
        while y>0:
            rem = y % 10
            y = int(y / 10)
            output.append(rem)
        revers = output[::-1]
        for i in range(len(revers)):
            temp = revers[i]*10**i
            the_number += temp

        if the_number<1<<31:
            if x < 0:
                return the_number * (-1)
            
            else:
                return the_number
        else:
            return 0

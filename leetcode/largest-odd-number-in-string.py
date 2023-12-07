class Solution:
    def largestOddNumber(self, num: str) -> str:
        the_out = ''
        out = ''
        if int(num[-1]) % 2 != 0:
          return num

        for i in num:
            the_out += i
            if int(i) % 2 != 0:
              out = the_out

        return out
        
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1 , num2 = num1[::-1], num2[::-1]
        mapper = {
            "1":1,
            "2":2,
            "3":3,
            "4":4,
            "5":5,
            "6":6,
            "7":7,
            "8":8,
            "9":9,
            "0":0,
        }
        int_1 = int_2 = 0
        
        out_put = ''
        for i in range(len(num1)):
            int_1 += mapper[num1[i]]*10**i
            print(mapper[num1[i]])

        for j in range(len(num2)):
            int_2 += mapper[num2[j]]*10**j
        the_sum = int_1 * int_2

        while the_sum>0:
            rem = the_sum % 10
            the_sum = the_sum // 10
            out_put += str(rem)
        return out_put[::-1]
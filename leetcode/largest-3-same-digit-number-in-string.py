class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_imum = 0
        flag = False
        for i in range(len(num)-2):
            if set(num[i:i+3]).__len__() == 1:
                flag = True
                max_imum = max(max_imum, int(num[i]))

        return str(max_imum)*3 if flag else ''
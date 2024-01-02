class Solution:
    def smallestNumber(self, num: int) -> int:
        if num > 0:
            my_list = [*str(num)]
            my_list.sort()
            if len(my_list) > 1:
                i = 0
                while my_list[i] == '0':
                    i += 1
                my_list[i], my_list[0] = my_list[0], my_list[i]
            if len(my_list) == 1:
                return num
            return int(''.join(my_list))
        else:
            my_list = [*str(abs(num))]
            my_list.sort(reverse = True)
            return - int(''.join(my_list))
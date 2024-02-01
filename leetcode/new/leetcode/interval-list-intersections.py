class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        first_pointer = second_pointer =  0
        res = []
        while first_pointer < len(firstList) and second_pointer < len(secondList):
            f_s, f_e = firstList[first_pointer]
            s_s, s_e = secondList[second_pointer]
            if s_s <= f_e and f_s <= s_e:
                res += [[max(f_s, s_s), min(f_e, s_e)]]

            if f_e <= s_e:
                first_pointer += 1
            else:
                
                second_pointer += 1

        return res
        
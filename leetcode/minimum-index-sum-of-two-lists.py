class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        out = []
        contaner = []
        for i in range(list1.__len__()):
            if list1[i] in list2:
                contaner.append(list1[i])

        max_index_sum = float('inf')

        for i in contaner:
            max_index_sum = min(max_index_sum, list1.index(i) + list2.index(i))

        for i in contaner:
            if list1.index(i) + list2.index(i) == max_index_sum:
                out.append(i)

        return out

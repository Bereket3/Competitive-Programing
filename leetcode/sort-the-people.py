class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # def selectionSort(array, size):
        #     for ind in range(size):
        #         min_index = ind
        
        #         for j in range(ind + 1, size):
        #             if array[j] < array[min_index]:
        #                 min_index = j
        #         array[ind], array[min_index] = array[min_index], array[ind]
        mapper = {}
        for i in range(len(names)):
            mapper[heights[i]] = names[i]
        heights.sort()
        return [mapper[i] for i in heights[::-1]]
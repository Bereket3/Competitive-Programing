class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        x, k = len(arr), []

        for i in range(x):
            max_ = max(arr[:x - i])
            max_indx = arr.index(max_) + 1
            arr[:max_indx] = reversed(arr[:max_indx])
            k.append(max_indx)
            arr[:x - i] = reversed(arr[:x - i])
            k.append(x - i)
        return k
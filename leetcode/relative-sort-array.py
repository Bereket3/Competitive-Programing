class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counted = Counter(arr2)
        is_not_in = []
        for i in range(arr1.__len__()):
            if arr1[i] in counted:
                counted[arr1[i]] += 1
            else:
                is_not_in.append(arr1[i])

        is_not_in.sort()
        new = []
        for i in counted:
            new += [i]*(counted[i] - 1)
        return new + is_not_in
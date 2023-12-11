class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        occurence_count = Counter(arr)
        return occurence_count.most_common(1)[0][0]
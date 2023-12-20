class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        the_str = ''.join(list(map(str, digits)))
        the_int = int(the_str) + 1
        the_str = str(the_int)
        digits = [ int(i) for i in the_str]
        return digits
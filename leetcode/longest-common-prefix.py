class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        out = '';  small_len = min(strs, key = len)

             
        for indx, char in enumerate(small_len):
            if all(strs[i][indx] == small_len[indx] for i in range(len(strs))):
                out += char
            else: break

        return out
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out = []
        small_len = min([word1, word2], key = len)
        last_index = small_len.__len__()
        for i in range(len(small_len)):
            out.append(word1[i]); out.append(word2[i])

        if word1.__len__() > last_index:
            out.append(word1[last_index:])
        elif word2.__len__() > last_index:
            out.append(word2[last_index:])

        return ''.join(out)
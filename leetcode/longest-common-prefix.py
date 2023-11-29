class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        minmum = min(list(map(len, strs)))
        splied = list(map(lambda x: x[:minmum], strs))
        something = []
        for j,i in enumerate(range(minmum)):
            try:something += [list(map(lambda x: x[j], splied))]
            except:...
        for i in something:
            if len(set(i)) == 1:result+=str(i[0])
            else:break
        return result
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        last = None
        for c in typed:
            if i < len(name) and c == name[i]:
                last = c
                i += 1
            elif c == last:
                continue
            else:
                return False
        return i == len(name)
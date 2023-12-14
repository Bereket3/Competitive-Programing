class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return set(s).__len__()
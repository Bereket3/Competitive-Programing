class Solution:
    def sortSentence(self, s: str) -> str:
        sent = s[::-1].split()
        sent.sort()
        return ' '.join([i[1:][::-1] for i in sent])
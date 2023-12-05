class Solution:
    def printVertically(self, s: str) -> List[str]:
        list_of_words = s.split()
        max_word_length = max(list_of_words, key = len)
        current_str = []
        new_contaner = []
        for i in range(len(max_word_length)):
            for j in list_of_words:
                try:
                    current_str.append(j[i])
                except:
                    current_str.append(' ')
            
            new_contaner.append(''.join(current_str))
            current_str = []

        return [i.rstrip() for i in new_contaner]
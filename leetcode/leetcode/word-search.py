class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R = len(board)
        C = len(board[0])
        
        if len(word) > R*C:
            return False
        
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
             
        n = len(board)
        m = len(board[0])
        p = set()

        def help(x, y, index):
            if index == len(word):
                return True
            
            if x >= n or y >= m:
                return False
            
            if tuple([x, y]) in p:
                return False
            
            if x < 0 or y < 0:
                return False
            
            if word[index] != board[x][y]:
                return False

            p.add((x, y))
            res = help(x + 1, y, index + 1) or help(x - 1, y, index + 1) or help(x, y - 1, index + 1) or help(x, y + 1, index + 1)
            p.remove((x, y))
            return res
        for i in range(n):
            for j in range(m):
                if help(i, j, 0):
                    return True
        return False
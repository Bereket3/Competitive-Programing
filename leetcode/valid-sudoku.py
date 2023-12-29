class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i, j in enumerate(zip(*board)):
            the_list = [int(k) for k in j if k != '.']
            if len(the_list) != len(set(the_list)):
                return False

        for i, j in enumerate(board):
            the_list = [int(k) for k in j if k != '.']
            if len(the_list) != len(set(the_list)):
                return False
        the_lists = [[], [], []]
        for i, j in enumerate(board):
            if (i+1)%3 == 0:
                the_lists[0] +=[int(i) for i in j[:3] if i != '.']
                the_lists[1] += [int(i) for i in j[3:6] if i != '.']
                the_lists[2] +=[int(i) for i in j[6:] if i != '.']
                for i in the_lists:
                    if len(i) != len(set(i)):
                        return False
                the_lists = [[], [], []]
            else:
                the_lists[0] +=[int(i) for i in j[:3] if i != '.']
                the_lists[1] += [int(i) for i in j[3:6] if i != '.' ]
                the_lists[2] +=[int(i) for i in j[6:] if i != '.']


        return True
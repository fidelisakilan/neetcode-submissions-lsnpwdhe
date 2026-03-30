class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_square = defaultdict(set)
        dict_x = defaultdict(set)
        dict_y = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board[0])):
                e = board[i][j]
                if e == ".":
                    continue
                if e in dict_x[i]:
                    return False
                if e in dict_y[j]:
                    return False
                if e in dict_square[(i//3,j//3)]:
                    return False
                dict_x[i].add(e)
                dict_y[j].add(e)
                dict_square[(i//3,j//3)].add(e)
        return True
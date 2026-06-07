class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)
        for i in range(len(board)):
            for j in range(len(board)):
                item = board[i][j]
                if item == ".":
                    continue
                if item in row[i]:
                    return False
                if item in col[j]:
                    return False
                if item in sqr[(i // 3, j // 3)]:
                    return False
                row[i].add(item)
                col[j].add(item)
                sqr[(i // 3, j // 3)].add(item)
                print(row, col, sqr)
        return True
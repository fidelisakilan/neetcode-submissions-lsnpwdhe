class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)
        rowMap = defaultdict(set)
        colMap = defaultdict(set)
        sqrMap = defaultdict(set)
        for i in range(l):
            for j in range(l):
                if board[i][j] == '.':
                    continue
                if board[i][j] not in rowMap[i]:
                    rowMap[i].add(board[i][j])
                else:
                    print('1')
                    print(i, j, rowMap[i])
                    return False
                if board[i][j] not in colMap[j]:
                    colMap[j].add(board[i][j])
                else:
                    print('2')
                    return False
                if board[i][j] not in sqrMap[tuple([i//3, j//3])]:
                    sqrMap[tuple([i//3, j//3])].add(board[i][j])
                else:
                    print('3')
                    return False
        return True
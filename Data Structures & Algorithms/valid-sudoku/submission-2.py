class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        collection_matrices = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            collection_by_row = set()
            collection_by_col = set()
            for j in range(9):
                if board[i][j] != ".": 
                    if board[i][j] in collection_matrices[i // 3][j // 3]:
                        print(i, j, i // 3, j // 3, board[i][j], collection_matrices[i // 3][j // 3])
                        return False
                    else:
                        collection_matrices[i // 3][j // 3].add(board[i][j])
                    if board[i][j] in collection_by_row:
                        return False
                    else: 
                        collection_by_row.add(board[i][j])
                
                if board[j][i] != ".":
                    if board[j][i] in collection_by_col:
                        return False
                    else:
                        collection_by_col.add(board[j][i])
        return True
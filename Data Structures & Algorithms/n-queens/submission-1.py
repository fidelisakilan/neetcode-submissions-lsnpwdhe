class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for i in range(n)]
        col = set()
        pos = set()
        neg = set()

        def backtrack(r):
            if r == n:
                new_board = ["".join(row) for row in board]
                res.append(new_board)
                return
            for c in range(n):
                if c not in col and (r+c) not in pos and (r-c) not in neg:
                    col.add(c)
                    pos.add(r+c)
                    neg.add(r-c)
                    board[r][c] = "Q"
                    
                    backtrack(r+1)
                    
                    col.remove(c)
                    pos.remove(r+c)
                    neg.remove(r-c)
                    board[r][c] = "."

        backtrack(0)
        return res

    
        
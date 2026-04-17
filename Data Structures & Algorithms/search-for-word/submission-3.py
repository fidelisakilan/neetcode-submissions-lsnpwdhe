class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking works here  by going into all its neighbours 
        # and seeing if element is available, if yes, then proceed to next items

        def backtrack(x, y, index):
            if index == len(word):
                return True
            if not 0 <= x < len(board[0]) or not 0 <= y < len(board):
                return False
            if word[index] == board[y][x]:
                temp = board[y][x]
                board[y][x] = "#"
                found = backtrack(x,y+1, index+1) or backtrack(x,y-1, index+1) or backtrack(x-1,y, index+1) or backtrack(x+1,y, index+1)
                board[y][x] = temp
                return found
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                found = backtrack(j,i, 0)
                if found == True:
                    return True
        return False

        
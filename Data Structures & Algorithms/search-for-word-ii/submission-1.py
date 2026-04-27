class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word):
        cur = self
        for letter in word:
            if letter not in cur.children:
                cur.children[letter] = TrieNode()
            cur = cur.children[letter]
        cur.isWord = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        row, col = len(board), len(board[0])
        res, visit = set(), set()
        print(row, col)
        for word in words:
            root.addWord(word)
        def dfs(r, c, node, word):
            if (
                r == row
                or c == col
                or r < 0
                or c < 0
                or (board[r][c] not in node.children)
                or ((r, c) in visit)
            ):
                return

            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for i in range(row):
            for j in range(col):
                dfs(i, j, root, "")

        return list(res)

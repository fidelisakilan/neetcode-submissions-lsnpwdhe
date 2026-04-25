class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = Node()        

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def backtrack(node, index):
            if index == len(word):
                print(word)
                return node.endOfWord
            ch = word[index]
            if ch != ".":
                if ch not in node.children:
                    return False
                return backtrack(node.children[ch], index + 1)
            else:
                for letter in node.children:
                    result = backtrack(node.children[letter], index + 1)
                    if result:
                        return True
            return False

        return backtrack(self.root, 0)
         
        

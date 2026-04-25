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
        cur = self.root
        result = False
        def backtrack(index):
            nonlocal result, cur
            if index == len(word):
                result = result or cur.endOfWord
                return
            if result: return
            if word[index] != ".":
                if word[index] not in cur.children:
                    return
                cur = cur.children[word[index]]
                backtrack(index+1)
            else:
                for letter in cur.children:
                    temp = cur
                    cur = cur.children[letter]
                    backtrack(index+1)
                    cur = temp
                
                

        backtrack(0)
        return result
         
        

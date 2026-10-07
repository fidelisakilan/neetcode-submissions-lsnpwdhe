class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for l in word:
            if l not in curr.children:
                curr.children[l] = TrieNode()
            curr = curr.children[l]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(node, word):
            curr = node
            for i, c in enumerate(word):
                if c == ".":
                    for child in curr.children.values():
                        if dfs(child, word[i+1:]):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.endOfWord
        return dfs(self.root, word)
        
        

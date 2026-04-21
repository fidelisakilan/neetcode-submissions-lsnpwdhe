class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        result = []
        seq = []
        t9 = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def dfs(index):
            if index == len(digits):
                result.append("".join(seq))
                return
            
            print(index, digits[index], t9[digits[index]])
            for letter in t9[digits[index]]:
                seq.append(letter)
                dfs(index+1)
                seq.pop()
        
        dfs(0)
        return result
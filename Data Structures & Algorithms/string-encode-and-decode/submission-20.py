class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            l = len(s)
            encoded = encoded + str(l) + "$" + s  
        return encoded

    def decode(self, s: str) -> List[str]:
        encoded_list = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j += 1
            
            l = int(s[i:j])
            i = j + 1
            j = i + l
            encoded_list.append(s[i:j])
            i = j
        return encoded_list


        

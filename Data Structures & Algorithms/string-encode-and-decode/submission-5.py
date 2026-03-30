class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for s in strs:
            encoded += f"= ={s}"
        return encoded
            

    def decode(self, s: str) -> List[str]:
        list_of_strings = []
        for word in s.split("= =")[1:]:
            list_of_strings.append(word)
        print(list_of_strings)
        return list_of_strings




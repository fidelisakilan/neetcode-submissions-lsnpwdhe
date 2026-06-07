class Solution:

    def encode(self, strs: List[str]) -> str:
        concat = ""
        for s in strs:
            length = len(s)
            concat += f"{length}#{s}"
        return concat

    def decode(self, s: str) -> List[str]:
        res = []
        while len(s):
            split_index = s.index("#")
            length = int(s[:split_index])
            res.append(s[split_index+1:split_index+length+1])
            # print(s, split_index, s[:split_index], s[split_index+1: length+2])
            s = s[split_index + length +1:]
        return res
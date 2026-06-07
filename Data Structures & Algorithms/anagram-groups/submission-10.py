class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            idx = [0] * 26
            for letter in s:
                idx[ord(letter) - ord('a')] += 1

            groups[tuple(idx)].append(s)
        print(list(groups.values()))
        return list(groups.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bucket = defaultdict(list)

        for s in strs:
            al = [0] * 26
            for c in s:
                al[ord(c) - ord("a")] += 1
            bucket[tuple(al)].append(s)
        return list(bucket.values())
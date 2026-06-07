class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)
        for s in strs:
            bucket = [0]*26
            for l in s:
                bucket[ord(l)-ord('a')] += 1
            group[tuple(bucket)].append(s)
        print(group)
        return list(group.values())
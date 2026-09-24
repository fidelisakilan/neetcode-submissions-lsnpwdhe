class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = defaultdict(int)
        for n in nums:
            bucket[n] += 1
        
        arr = []
        for key, v in bucket.items():
            arr.append((v, key))
        arr.sort()
        res = []
        while len(res) < k:
            print(arr[-1][1], k)
            res.append(arr.pop()[1])
        return res
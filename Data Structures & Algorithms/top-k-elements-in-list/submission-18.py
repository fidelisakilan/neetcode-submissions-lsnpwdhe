class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1
        
        bucket = [[] for _ in range(len(nums)+1)]
        
        for key, val in counter.items():
            bucket[val].append(key)
        res = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                res.append(num)
                print(res, k)
                if len(res) == k:
                    return res
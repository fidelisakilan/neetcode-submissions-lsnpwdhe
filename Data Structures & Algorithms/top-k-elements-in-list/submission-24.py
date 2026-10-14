class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = defaultdict(int)
        for n in nums:
            bucket[n] += 1
        heap = []
        for key, v in bucket.items():
            heapq.heappush(heap, (v, key))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.res = []
        self.k = k
        for n in nums:
            heapq.heappush(self.res, n)
            if len(self.res) > k:
                heapq.heappop(self.res)
        

    def add(self, val: int) -> int:
        print(self.res)
        heapq.heappush(self.res, val)
        if len(self.res) > self.k:
            heapq.heappop(self.res)
        return self.res[0]

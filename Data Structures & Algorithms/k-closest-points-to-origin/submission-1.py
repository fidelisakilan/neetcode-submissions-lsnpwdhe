class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for p in points:
            px, py = p
            distance = math.sqrt(px*px + py*py)
            heapq.heappush(heap, (distance, p))
        
        res = []
        while k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        return res
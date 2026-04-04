class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for point in points:
            x,y = point
            dist = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (dist, point))
        result = []
        while k > 0 and heap:
            value = heapq.heappop(heap)
            result.append(value[1])
            k -= 1
        return result

        
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for px, py in points:
            dist = math.sqrt(px*px + py*py)
            heapq.heappush(heap, (dist,[px,py]))
        print(heap)
        res = []
        while k > 0:
            a = heapq.heappop(heap)
            print(a)
            res.append(a[1])
            k -= 1
        return res
            
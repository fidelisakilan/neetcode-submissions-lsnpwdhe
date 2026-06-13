class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((w,v))
        
        visit = set()
        stack = [(0, k)]
        t = 0
        while stack:
            print(stack)
            w1, u1 = heapq.heappop(stack)
            if u1 in visit:
                continue

            visit.add(u1)
            t = w1
            for nei in edges[u1]:
                w2, v2 = nei
                if v2 not in visit:
                    heapq.heappush(stack, (w1 + w2, v2))
        return t if len(visit) == n else -1
        




        
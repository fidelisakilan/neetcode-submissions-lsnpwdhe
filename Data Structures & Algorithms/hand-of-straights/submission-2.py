class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        heap = []
        count = defaultdict(int)
        for h in hand:
            heapq.heappush(heap, h)
            count[h] += 1
        res = []
        while heap:
            curr = heap[0]
            group = []
            while len(group) < groupSize and count[curr] > 0:
                if count[curr] == 1:
                    if heap[0] != curr:
                        return False
                    while heap and heap[0] == curr:
                        heapq.heappop(heap)
                group.append(curr)
                count[curr] -= 1
                curr += 1
            if len(group) == groupSize:
                res.append(group)
            else:
                return False
        return True
        
            




                    

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # heap and a hashmap for frequency
        time = 0
        queue = deque()
        heap = [-count for count in Counter(tasks).values()]
        heapq.heapify(heap)
        print(heap)
        while heap or queue:
            # print(time, heap, queue)
            time += 1
            if heap:
                freq = -heapq.heappop(heap) - 1
                if freq > 0:
                    queue.append((freq, time + n))
            if queue and queue[0][1] == time:
                freq, _ = queue.popleft()
                heapq.heappush(heap, -freq)
        
        return time


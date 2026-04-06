class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        queue = deque([])

        while maxHeap or queue:
            if maxHeap:
                element = heapq.heappop(maxHeap)
                if element + 1 != 0:
                    queue.append((element + 1, time + n + 1))
            time += 1

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue[0][0])
                queue.popleft()
        return time 
        
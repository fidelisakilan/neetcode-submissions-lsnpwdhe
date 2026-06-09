class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # USING DEQUE
        output = []
        q = deque()
        l = r = 0
        while r < len(nums):
            # remove prev smaller numbers
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            # if topelement is out of scope remove it
            if l > q[0]:
                q.popleft()
            
            # if window is full add the max to output and slide
            if (r+1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
        
        # USING HEAP
        # heap = []
        # output = []
        # for i, n in enumerate(nums):
        #     heapq.heappush(heap, (-n, i))
        #     if i >= k-1:
        #         while heap[0][1] <= i-k:
        #             heapq.heappop(heap)
        #         output.append(-heap[0][0])
        # return output

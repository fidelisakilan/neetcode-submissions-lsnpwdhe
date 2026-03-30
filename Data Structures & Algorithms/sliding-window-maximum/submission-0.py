class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        l, r = 0, 0
        res = []

        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            q.append(r)

            # remove leftmost from the window if l index is higher
            if l > q[0]:
                q.popleft()

            # add top element to max
            if r+1 >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res
        
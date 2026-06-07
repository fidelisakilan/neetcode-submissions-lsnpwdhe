class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()

        # it is a decreasing order of queue
        # add a element to the right if it is less than top
        # if first element in the queue is out of window, remove it
        # at end of each window get the first element which is the highest element
        # if the new element is the greatest, lets pop smaller values from the queue
        l = 0
        res = []
        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                l += 1
                res.append(nums[q[0]])
        return res


        
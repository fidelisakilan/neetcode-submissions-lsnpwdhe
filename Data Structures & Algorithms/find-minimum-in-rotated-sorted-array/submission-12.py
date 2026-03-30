# First get l = 0 and r = len - 1
# if l <= r then get l and check for min
# get the mid point m 
# see if m value is > than l value
# if then l = m + 1
# otherwise r = m - 1
# reason is that if its in order then smallest value is on the other side

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return nums[l]
        
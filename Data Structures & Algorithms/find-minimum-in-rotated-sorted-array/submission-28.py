class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float("inf")
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            print(l, mid, r)
            if nums[l] <= nums[r]:
                res = min(res, nums[l])
                break
            res = min(res, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        if res != float("inf"):
            return res
        else:
            return -1
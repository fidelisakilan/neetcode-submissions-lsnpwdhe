class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        mid = left 
        def binary_search(n, target):
            print(n, target)
            l, r = 0, len(n) - 1
            while l <= r:
                m = (l + r) // 2
                if n[m] == target:
                    return m
                elif target > n[m]:
                    l = m + 1
                elif target < n[m]:
                    r = m - 1
            return -1
        res1 = binary_search(nums[:mid], target)
        res2 = binary_search(nums[mid:], target)
        if res1 != -1:
            return res1
        if res2 != - 1: 
            return mid + res2
        return - 1

        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
            
        pivot = l

        def binary_search(nums, target) -> int:
            l, r = 0, len(nums) - 1
            print(l, r, nums)
            while l <= r:
                mid = (l + r) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
            return -1
        
        res = binary_search(nums[:pivot], target)
        if res != -1:
            return res

        res = binary_search(nums[pivot:], target)
        if res != -1:
            return res + pivot
        return -1
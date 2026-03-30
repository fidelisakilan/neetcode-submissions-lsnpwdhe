class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            # left series, target greater than series
            elif nums[mid] >= nums[l] and target > nums[mid]:
                l = mid + 1
            # left series, target less than mid
            elif nums[mid] >= nums[l] and target < nums[mid]:
                # if target greater than first element
                if target >= nums[l]:
                    r = mid - 1
                # if target less than first element
                else:
                    l = mid + 1
            # right series, target greater than mid
            elif nums[mid] < nums[l] and target > nums[mid]:
                # if target within last element of the list
                if target <= nums[r]:
                    l = mid + 1
                # if target is greater than last element of the list
                else:
                    r = mid - 1
            # right series, targer less than mid
            elif nums[mid] < nums[l] and target < nums[mid]:
                r = mid - 1 
        return -1
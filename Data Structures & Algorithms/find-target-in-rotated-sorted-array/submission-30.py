class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # take left and right
        # if mid == target then found
        # if left array is sorted, then see if target is either less than l or greater than mid, then move l to mid + 1 otherwise move r to mid -1
        # do the same for right array
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target > nums[right] or target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        mini = 999
        while left <= right:
            if nums[left] <= nums[right]:
                mini = min(mini, nums[left])
                break
            
            mid = (left + right) // 2
            mini = min(mini, nums[mid])

            if nums[left]  <= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return mini

        
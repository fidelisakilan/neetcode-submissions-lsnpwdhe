class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = set()
        for i in range(0, len(nums)-2):
            j, k = i+1, len(nums) -1
            target = -nums[i]
            while j < k:
                sumof = nums[j] + nums[k]
                if target > sumof:
                    j += 1
                elif target < sumof:
                    k -= 1
                else:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
            
        return list(res)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        groups = set()
        nums.sort()
        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                subtotal = nums[j] + nums[k]
                if subtotal > target:
                    k -= 1
                elif subtotal < target:
                    j += 1
                else:
                    groups.add(tuple([nums[i],nums[j],nums[k]]))
                    j += 1
                    k -= 1
        return list(groups)
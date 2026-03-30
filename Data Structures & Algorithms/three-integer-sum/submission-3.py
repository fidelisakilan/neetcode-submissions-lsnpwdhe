class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            l = i + 1
            r = len(nums) - 1
            while (l < r):
                three_sum = nums[l] + nums[r] + target
                if three_sum == 0:
                    triplets.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif three_sum < 0:
                    l += 1
                else:
                    r -= 1
        return triplets
            

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        n = len(nums)
        nums.sort()
        for i in range(0, n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = n - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                # print(total)
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    combinations.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
        return combinations

        
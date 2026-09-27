class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def dfs(i, prev, count):
        #     if i >= len(nums):
        #         return count
        #     if prev is not None and nums[i] <= prev:
        #         return max(dfs(i+1, prev, count), dfs(i+1, nums[i], 1))
        #     else:
        #         return max(dfs(i+1, prev, count),dfs(i+1, nums[i], count+1))        
        # return dfs(0, None, 0)


        LIS = [1]*len(nums)
        for i in range(len(nums)-1, -1, - 1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)


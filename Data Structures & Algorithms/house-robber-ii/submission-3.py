class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        def dfs(i, cache, end):
            if i >= end:
                return 0
            if cache[i] != -1:
                return cache[i]
            cache[i] = max(
                dfs(i+1, cache, end), 
                nums[i] + dfs(i+2, cache, end)
                )
            return cache[i]
        

        return max(
            dfs(0, [-1]*len(nums), len(nums)-1), 
            dfs(1, [-1]*len(nums), len(nums))
            )
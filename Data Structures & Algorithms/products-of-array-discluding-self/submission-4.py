class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     res = [0] * len(nums)
    #     pre = [0] * len(nums)
    #     suf = [0] * len(nums)

    #     pre[0] = 1
    #     suf[len(nums) - 1] = 1

    #     for idx in range(1, len(nums)):
    #         pre[idx] = nums[idx - 1] * pre[idx - 1]
        
    #     for idx in range(len(nums) - 2, -1, -1):
    #         suf[idx] = nums[idx + 1] * suf[idx + 1]

    #     for idx in range(len(nums)):
    #         res[idx] = pre[idx] * suf[idx]
    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]


        return res

        
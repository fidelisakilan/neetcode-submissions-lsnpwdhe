class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    # def hasDuplicate(self, nums: List[int]) -> bool:
    #     for i in range(len(nums)):
    #         for j in range(len(nums) - 1):
    #             if i == j:
    #                 continue
    #             if nums[i] == nums[j]:
    #                 return True
    #     return False


    
         
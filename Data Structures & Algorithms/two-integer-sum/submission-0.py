class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # First find if missing number is present in dict
        # if yes then return the index of target and current
        # else store the target to dict

        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict: 
                return [dict[nums[i]], i]
            else:
                number = target - nums[i]
                dict[number] = i
    
            
            


        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_dict = {}
        for idx, n in enumerate(nums):
            if target - n in diff_dict:
                return [diff_dict[target - n], idx]
            diff_dict[n] = idx

        
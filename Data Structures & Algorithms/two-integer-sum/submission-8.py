class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_map = {}
        for index, value in enumerate(nums):
            if target - value in diff_map:
                return [diff_map[target - value], index]
            elif value not in diff_map:
                diff_map[value] = index
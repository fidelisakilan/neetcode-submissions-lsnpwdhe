class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        sublist = self.permute(nums[1:])
        result = []
        for l in sublist:
            for i in range(0, len(l) + 1):
                l_copy = l.copy()
                l_copy.insert(i, nums[0])
                result.append(l_copy)
        return result

        
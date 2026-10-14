class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()

        for n in nums:
            hashset.add(n)
        res = 0
        for i in range(len(nums)):
            counter = 0
            j = nums[i]
            if nums[i] - 1 not in hashset:
                while j in hashset:
                    counter += 1
                    j += 1
            res = max(res, counter)
        return res


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        number_set = set(nums)
        longest = 0
        for n in nums:
            if n - 1 not in number_set:
                length = 0
                while(n + length) in number_set:
                    length +=1
                longest = max(length, longest)
        return longest
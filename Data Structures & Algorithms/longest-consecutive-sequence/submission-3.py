class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     hash_set = set(nums)
    #     longest = 0
    #     for i in nums:
    #         if i - 1 not in hash_set:
    #             length = 0
    #             while i + length in hash_set:
    #                 length += 1
    #             longest = max(length, longest)
    #     return longest

    def longestConsecutive(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        longest = 0
        for n in nums:
            if mp[n] == 0:
                mp[n] = mp[n-1] + mp[n+1] + 1
                mp[n - mp[n-1]] = mp[n]
                mp[n + mp[n+1]] = mp[n]
                longest = max(mp[n], longest)
        return longest
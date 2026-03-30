class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = set()

        for n in nums:
            if n in nums_dict:
                return True
            nums_dict.add(n)
        return False
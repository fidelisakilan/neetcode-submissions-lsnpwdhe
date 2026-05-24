class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = set()
        for n in nums:
            if n in counter:
                return True
            counter.add(n)
        return False
            

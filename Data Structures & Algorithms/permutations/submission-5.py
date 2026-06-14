class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(perm, visit):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for i in range(len(nums)):
                if i not in visit:
                    perm.append(nums[i])
                    visit.add(i)
                    backtrack(perm, visit)
                    perm.pop()
                    visit.remove(i)
        backtrack([], set())
        return res
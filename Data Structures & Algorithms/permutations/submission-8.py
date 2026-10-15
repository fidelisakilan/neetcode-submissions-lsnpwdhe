class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        visit = set()
        sub = []
        def dfs():
            if len(sub) == len(nums):
                res.append(sub.copy())
                return
            for n in nums:
                if n in visit:
                    continue
                
                visit.add(n)
                sub.append(n)
                
                dfs()
                
                visit.remove(n)
                sub.pop()
        dfs()
        return res

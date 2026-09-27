class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        res = []
        def backtrack(sub):
            if len(sub) == len(nums):
                res.append(sub.copy())
                return

            for i in range(len(nums)):
                if i in visited:
                    continue
                visited.add(i)
                sub.append(nums[i])
                backtrack(sub)
                sub.pop()
                visited.remove(i)
        backtrack([])
        return res
        

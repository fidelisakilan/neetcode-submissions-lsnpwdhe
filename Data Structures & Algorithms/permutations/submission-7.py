class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        subres = []
        visited = set()
        def backtrack():
            for i in nums:
                if len(subres) == len(nums):
                    res.append(subres.copy())
                    return
                if i in visited:
                    continue
                visited.add(i)
                subres.append(i)
                backtrack()
                subres.pop()
                visited.remove(i)
        backtrack()
        return res
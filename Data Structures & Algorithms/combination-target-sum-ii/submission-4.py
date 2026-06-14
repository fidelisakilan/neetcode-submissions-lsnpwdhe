class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        items = []
        candidates.sort()

        def backtrack(index, total):
            if total == target:
                res.append(items.copy())
                return
            
            if index >= len(candidates) or total > target :
                return

            items.append(candidates[index])
            backtrack(index+1, total + candidates[index])
            items.pop()

            while index +1 < len(candidates) and candidates[index+1] == candidates[index]:
                index += 1
            backtrack(index+1, total)
            
        
        backtrack(0, 0)
        return res
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        seq = []
        candidates.sort()

        def dfs(index, total):
            if total == target:
                result.append(seq.copy())
                return
            if total > target or index == len(candidates):
                return
            
            seq.append(candidates[index])
            dfs(index+1, total+candidates[index])
            seq.pop()

            while index+1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index+1, total)

        dfs(0, 0)
        return result
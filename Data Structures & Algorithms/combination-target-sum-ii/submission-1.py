class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []
        subset = []

        def dfs(i, curr_result = 0):
            if curr_result == target:
                results.append(subset.copy())
                return
            elif curr_result > target or i == len(candidates):
                return

            subset.append(candidates[i])
            dfs(i+1, curr_result + candidates[i])

            subset.pop()

            while i < len(candidates)-1 and candidates[i] == candidates[i+1]:
                i += 1

            dfs(i+1, curr_result)

        dfs(0, 0)
        return results
        

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        subset = []

        def dfs(i, curr_result = 0):
            if curr_result == target:
                results.append(subset.copy())
                return
            elif curr_result > target or i == len(nums):
                return

            subset.append(nums[i])
            dfs(i, curr_result + nums[i])

            subset.pop()
            dfs(i+1, curr_result)

        dfs(0, 0)
        return results


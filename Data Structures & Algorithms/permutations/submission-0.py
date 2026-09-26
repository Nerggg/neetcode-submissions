class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        subset = []

        def dfs():
            if len(subset) == len(nums):
                results.append(subset.copy())
                return

            for n in nums:
                if n in subset: continue
                subset.append(n)
                dfs()
                subset.pop()


        dfs()
        return results


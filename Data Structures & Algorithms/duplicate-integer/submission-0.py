class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for n in nums:
            if n in memo:
                return True
            else:
                memo[n] = True
        return False
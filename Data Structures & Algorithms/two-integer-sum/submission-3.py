class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        r = len(nums)
        
        while r > 0:
            for i in range (0, r - 1):
                if nums[i] + nums[r - 1] == target:
                    return [i, r - 1]
            r -= 1

        return []

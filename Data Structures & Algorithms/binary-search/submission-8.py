class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            find_idx = l + (r - l) // 2
            find = nums[find_idx]
            if find == target:
                return find_idx
            elif find < target:
                l = find_idx + 1
            else:
                r = find_idx - 1
        return -1

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        min_val = nums[0]
        while l < r:
            if r == l + 1:
                return min(nums[l], nums[r])
            mid = l + (r - l) // 2
            if mid < min_val: min_val = mid
            if nums[mid] > nums[l] and nums[mid] > nums[r]:
                l = mid
            elif nums[mid] < nums[l] and nums[mid] < nums[r]:
                r = mid
            elif nums[mid] > nums[l] and nums[mid] < nums[r]:
                return nums[l]

        return min_val

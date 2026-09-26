class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        max_val = 0

        while l < r:
            curr_val = min(heights[l], heights[r]) * (r - l)
            if curr_val > max_val:
                max_val = curr_val

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return max_val


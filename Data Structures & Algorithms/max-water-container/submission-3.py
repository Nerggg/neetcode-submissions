class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if (len(heights) == 0): return 0
        l = 0
        r = len(heights) - 1

        result = 0
        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            if result < curr:
                result = curr

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return result

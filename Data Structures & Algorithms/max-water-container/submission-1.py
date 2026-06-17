class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        f = 0
        b = n - 1

        result = 0
        while f < b:
            temp = (b - f) * min(heights[f], heights[b])
            if temp > result:
                result = temp

            if heights[f] > heights[b]:
                b -= 1
            else:
                f += 1

        return result

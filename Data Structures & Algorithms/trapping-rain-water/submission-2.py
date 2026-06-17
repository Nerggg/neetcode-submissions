class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)

        l_max = height[0]
        r_max = height[n-1]

        l = 0
        r = n-1

        while l < r:
            if l_max < r_max:
                l += 1
                if height[l] >= l_max:
                    l_max = height[l]
                    continue
                else:
                    result += (min(l_max, r_max) - height[l])
            else:
                r -= 1
                if height[r] >= r_max:
                    r_max = height[r]
                    continue
                else:
                    result += (min(l_max, r_max) - height[r])

        return result

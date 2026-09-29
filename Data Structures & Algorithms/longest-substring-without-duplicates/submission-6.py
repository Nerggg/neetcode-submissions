
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        r = 0
        max_result = 0

        while r < len(s):
            while s[r] in seen and seen[s[r]]:
                seen[s[l]] = False
                l += 1

            seen[s[r]] = True

            window_size = r - l + 1
            if window_size > max_result:
                max_result = window_size

            r += 1

        return max_result



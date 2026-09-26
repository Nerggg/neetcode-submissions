
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        l = 0
        seen = {s[0]: True}
        max_val = 1

        for r in range (1, n):
            while s[r] in seen and seen[s[r]]:
                seen[s[l]] = False
                l += 1

            seen[s[r]] = True

            window_size = r - l + 1
            if window_size > max_val:
                max_val = window_size

        return max_val


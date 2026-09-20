class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l = 0
        max_result = 0
        for r in range(len(s)):
            # print("char_set:", char_set)
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1

            char_set.add(s[r])

            window_size = r - l + 1
            if window_size > max_result:
                max_result = window_size

        return max_result

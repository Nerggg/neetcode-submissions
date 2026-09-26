class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_dict = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] not in freq_dict:
                freq_dict[s[r]] = 1
            else:
                freq_dict[s[r]] += 1

            while (r - l + 1) - max(freq_dict.values()) > k:
                freq_dict[s[l]] -= 1
                l += 1

            curr_len = r - l + 1
            if curr_len > max_len:
                max_len = curr_len

        return max_len

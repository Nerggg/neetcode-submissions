class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        frequency = {}
        max_result = 0

        for r in range(len(s)):
            print()
            if s[r] not in frequency:
                frequency[s[r]] = 1
            else:
                frequency[s[r]] += 1

            while ((r - l + 1) - max(frequency.values())) > k:
                frequency[s[l]] -= 1
                l += 1
                # print("max_result:", max_result)
                # print("l:", l)
                # print("r:", r)
                # print("frequency:", frequency)

            current_length = r - l + 1
            if current_length > max_result:
                max_result = current_length
                # print("max_result berubah jadi:", max_result)
                # print("l:", l)
                # print("r:", r)


        # print("frequency:", frequency)
        # print("l:", l)
        return max_result

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        arr_s1 = [0] * 26
        arr_s2 = [0] * 26

        for i in range(len(s1)):
            arr_s1[ord(s1[i]) - ord('a')] += 1
            arr_s2[ord(s2[i]) - ord('a')] += 1

        if arr_s1 == arr_s2: 
            return True

        for i in range(len(s1), len(s2)):
            char_in = s2[i]
            char_out = s2[i - len(s1)]

            arr_s2[ord(char_in) - ord('a')] += 1
            arr_s2[ord(char_out) - ord('a')] -= 1

            if arr_s1 == arr_s2: 
                return True

        return False

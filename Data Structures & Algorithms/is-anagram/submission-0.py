class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        memo_s = {}
        for elm in s:
            if elm not in memo_s:
                memo_s[elm] = 1
            else:
                memo_s[elm] += 1

        memo_t = {}
        for elm in t:
            if elm not in memo_t:
                memo_t[elm] = 1
            else:
                memo_t[elm] += 1

        if memo_s == memo_t:
            return True
        else:
            return False
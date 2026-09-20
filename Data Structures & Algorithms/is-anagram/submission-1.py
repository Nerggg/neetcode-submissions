class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_memo = {}
        t_memo = {}
        for s_char in s:
            if s_char in s_memo:
                s_memo[s_char] += 1
            else:
                s_memo[s_char] = 1

        for t_char in t:
            if t_char in t_memo:
                t_memo[t_char] += 1
            else:
                t_memo[t_char] = 1
        
        return s_memo == t_memo

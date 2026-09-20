class Solution:
    def isAlphanumeric(self, c: str) -> bool:
        return c in "abcdefghijklmnopqrstuvwxyz0123456789"
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l <= r:
            if not self.isAlphanumeric(s[l]): 
                l += 1
                continue
            elif not self.isAlphanumeric(s[r]): 
                r -= 1
                continue
            elif s[l] != s[r]: 
                # print(s[l])
                # print(s[r])
                return False
            l += 1
            r -= 1

        return True

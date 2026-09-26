
class Solution:
    def __isAlphanumeric(self, c: str) -> bool:
        return c in "abcdefghijklmnopqrstuvwxyz0123456789"

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not self.__isAlphanumeric(s[l]):
                l += 1
            while l < r and not self.__isAlphanumeric(s[r]):
                r -= 1

            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True

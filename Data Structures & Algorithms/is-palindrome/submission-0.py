class Solution:
    def isAlphanumeric(self, c: str) -> bool:
        return c in "abcdefghijlkmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_clean = ""
        for c in s:
            if self.isAlphanumeric(c):
                s_clean += c

        front = 0
        back = len(s_clean) - 1

        while front <= back:
            if s_clean[front] != s_clean[back]:
                return False

            front += 1
            back -= 1

        return True

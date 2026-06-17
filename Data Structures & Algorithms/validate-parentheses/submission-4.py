class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        stack = []
        for char in s:
            print(stack)
            if char in "({[":
                stack.append(char)

            elif not stack: return False
            elif char == ")" and stack.pop() != "(": return False
            elif char == "}" and stack.pop() != "{": return False
            elif char == "]" and stack.pop() != "[": return False

        return not stack

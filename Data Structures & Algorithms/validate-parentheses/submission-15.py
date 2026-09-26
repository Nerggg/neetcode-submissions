class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 != 0: return False
        for char in s:
            if char == '(': stack.append(char)
            elif char == '{': stack.append(char)
            elif char == '[': stack.append(char)

            if len(stack) == 0: return False

            elif char == ')' and stack.pop(-1) != '(': return False
            elif char == ']' and stack.pop(-1) != '[': return False
            elif char == '}' and stack.pop(-1) != '{': return False

        return len(stack) == 0
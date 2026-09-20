class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) // 2 == 0: return False

        stack = []
        for char in s:
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            elif (len(stack) == 0) or (char == ')' and stack.pop() != '(') or (char == '}' and stack.pop() != '{') or (char == ']' and stack.pop() != '['):
                return False

        return len(stack) == 0

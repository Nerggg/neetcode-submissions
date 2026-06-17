class Solution:
    def is_number(self, string):
        try:
            float(string)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            # print(f"stack: ", stack)
            if self.is_number(t):
                stack.append(t)
            else:
                if t == "+":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num1 + num2)
                elif t == "-":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 - num1)
                elif t == "/":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num2 / num1)
                elif t == "*":
                    num1 = int(stack.pop())
                    num2 = int(stack.pop())
                    stack.append(num1 * num2)

        return int(stack[0])

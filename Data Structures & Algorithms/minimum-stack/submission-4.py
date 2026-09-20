class MinStack:
    stack: List[int]
    min_stack: List[int]

    def __init__(self):
        self.stack = []
        self.min_stack = []
        return None

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack:
            if val < self.min_stack[-1]:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)

        # print("stack after append:", self.stack)
        # print("min_stack after append:", self.min_stack)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * (len(temperatures) - 1)
        for i in range (len(temperatures)):
            if i == 0:
                stack.append(i)
                result.append(0)
                continue

            while stack and temperatures[i] > temperatures[stack[-1]]:
                result[stack[-1]] = i - stack[-1]
                stack.pop()

            stack.append(i)

        return result

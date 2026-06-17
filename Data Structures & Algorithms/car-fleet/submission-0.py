class Solution:
    def bubbleSort(self, pos, speed):
        swapped = False
        n = len(pos)
        for i in range (n):
            for j in range (n - 1 - i):
                if pos[j] < pos[j+1]:
                    pos[j], pos[j+1] = pos[j+1], pos[j]
                    speed[j], speed[j+1] = speed[j+1], speed[j]
                    swapped = True

            if not swapped:
                break

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        self.bubbleSort(position, speed)
        n = len(position)
        stack = []

        for i in range (n):
            p = position[i]
            s = speed[i]

            time = (target - p) / s

            if stack and time <= stack[-1]:
                continue

            stack.append(time)

        # print(stack)
        return len(stack)

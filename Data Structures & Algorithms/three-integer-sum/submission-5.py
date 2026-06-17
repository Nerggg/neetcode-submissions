class Solution:
    def bubbleSort(self, l):
        n = len(l)
        for i in range (n):
            swapped = False
            for j in range (n - i - 1):
                if l[j] > l[j+1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    swapped = True

            if not swapped:
                break

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.bubbleSort(nums)
        result = []
        n = len(nums)

        for i in range (n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            front = i + 1
            back = n - 1

            while front < back:
                # print(f"front: ", front)
                # print(f"back: ", back)
                if nums[i] + nums[front] + nums[back] == 0:
                    result.append([nums[i], nums[front], nums[back]])
                    front += 1
                    while front < back and nums[front] == nums[front-1]:
                        front += 1

                elif nums[i] + nums[front] + nums[back] < 0:
                    front += 1

                else:
                    back -= 1

        return result

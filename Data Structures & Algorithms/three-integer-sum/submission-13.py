class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1

            while l < r:
                calc = nums[i] + nums[l] + nums[r]
                # print("i:", i)
                # print("l:", l)
                # print("r:", r)
                # print("calc:", calc)
                # print()
                if calc == 0:
                    temp = [nums[i], nums[l], nums[r]]
                    if temp not in result:
                        result.append(temp)
                    l += 1
                elif calc > 0:
                    r -= 1
                else: # calc < 0
                    l += 1
        return result

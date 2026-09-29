class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if temp in d:
                return [d[temp] + 1, i + 1]

            d[numbers[i]] = i
        

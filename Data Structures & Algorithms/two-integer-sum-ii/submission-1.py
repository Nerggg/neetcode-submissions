class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dct = {}
        for i in range (len(numbers)):
            dct[numbers[i]] = i + 1

        for i in range (len(numbers)):
            if target - numbers[i] in dct:
                if i+1 > dct[target - numbers[i]]:
                    return [dct[target - numbers[i]], i+1]
                else:
                    return [i+1, dct[target - numbers[i]]]

        return []

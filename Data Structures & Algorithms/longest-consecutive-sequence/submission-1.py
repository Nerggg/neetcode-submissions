class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dct = {}
        for n in nums:
            dct[n] = True
    
        max_result = 0
        for n in nums:
            result = 1
            temp = n + 1
            while temp in dct:
                result += 1
                temp += 1

            if result > max_result:
                max_result = result

        return max_result

class Solution:
    def calcHour(self, piles, rate):
        hour_taken = 0
        for p in piles:
            # division = p // rate
            # print(f"division for rate {rate}: ", division)
            hour_taken += p // rate
            if p % rate != 0: hour_taken += 1

        return hour_taken

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_val = max(piles)
        # print(f"search_list: ", search_list)
        min_result = max_val
        
        l = 1
        r = max_val

        while l <= r:
            mid = l + (r - l) // 2

            current_hour_taken = self.calcHour(piles, mid)
            # print(f"search_list[mid]: ", search_list[mid])
            # print(f"current_hour_taken: ", current_hour_taken)

            if current_hour_taken <= h: # rate is high enough, meaning we should move the right pointer
                r = mid - 1
                if mid < min_result: 
                    min_result = mid
            else: # rate is too low because current_hour_taken is longer than the needed hour
                l = mid + 1

        return min_result

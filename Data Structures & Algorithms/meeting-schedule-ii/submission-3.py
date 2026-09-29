class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_arr = sorted([i.start for i in intervals])
        s = 0
        end_arr = sorted([i.end for i in intervals])
        e = 0
        room = 0
        result = 0

        while s < len(intervals):
            if start_arr[s] < end_arr[e]:
                room += 1
                s += 1
            else:
                room -= 1
                e += 1

            result = room if room > result else result

        return result

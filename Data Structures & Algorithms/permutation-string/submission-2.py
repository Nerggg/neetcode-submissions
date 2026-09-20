class Solution:
    def copyDict(self, d) -> dict:
        result = {}
        for key, value in d.items():
            result[key] = value
        return result

        return result
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}
        for s in s1:
            if s not in freq_map:
                freq_map[s] = 1
            else:
                freq_map[s] += 1

        window_l = -1
        window_r = len(s1) - 1
        # print("window_l:", window_l)
        # print("window_r:", window_r)
        # print("len(s2) - len(s1):", len(s2) - len(s1))

        # print("freq_map:", freq_map)

        for i in range(len(s2) - len(s1) + 1):
            freq_map_copy = self.copyDict(freq_map)
            window_l += 1
            window_r += 1

            # print("s2[window_l]:", s2[window_l])
            # print("s2[window_r - 1]:", s2[window_r - 1])
            if s2[window_l] in freq_map:
                # print("masuk pas window_l nya", s2[window_l])
                for j in range(window_l, window_r):
                    # print("j:", j)
                    if s2[j] not in freq_map or freq_map[s2[j]] == 0:
                        freq_map_copy = self.copyDict(freq_map)
                        # print("break pas j", j)
                        break

                    freq_map_copy[s2[j]] -= 1
                    # print(f"s2[j] {s2[j]} decreased")

                if max(freq_map_copy.values()) == 0: 
                    # print("freq_map_copy:", freq_map_copy)
                    # print("freq_map:", freq_map)
                    # print("window_l:", window_l)
                    # print("window_r:", window_r)
                    return True
                else:
                    freq_map_copy = self.copyDict(freq_map)

        return False
            

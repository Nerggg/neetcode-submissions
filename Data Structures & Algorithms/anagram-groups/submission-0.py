class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memos = {}
        for word in strs:
            memos[word] = {}
            for w in word:
                if w not in memos[word]:
                    memos[word][w] = 1
                else:
                    memos[word][w] += 1

        result = []
        track = []
        
        for m in memos:
            temp_result = []
            for s in strs:
                if memos[m] == memos[s] and memos[m] not in track:
                    temp_result.append(s)

            if temp_result:
                result.append(temp_result)
                track.append(memos[m])

        return result

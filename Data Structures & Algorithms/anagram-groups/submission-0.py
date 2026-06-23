class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_copy = strs.copy()
        for i in range(len(strs)):
            strs[i] = ''.join(sorted(strs[i]))
        d = {}
        for i in range(len(strs)):
            if strs[i] not in d:
                d[strs[i]] = []
            d[strs[i]].append(strs_copy[i])
        
        result = []
        for i in d:
            result.append(d[i])
        print(result)
        return result

        
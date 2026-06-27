class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window_size = len(s1)
        hash1 = {}
        hash2 = {}
        for i in s1:
            hash1[i] = hash1.get(i,0)+1
        p1=0
        p2=len(s1)

        for i in range(len(s1)):
            hash2[s2[i]] = hash2.get(s2[i], 0) + 1
        while p2<len(s2):
            if hash1 == hash2:
                return True
            hash2[s2[p1]] -= 1

            if hash2[s2[p1]] == 0:
                del hash2[s2[p1]]
            hash2[s2[p2]] = hash2.get(s2[p2], 0) + 1
            p1+=1
            p2+=1
        if hash1 == hash2:
            return True
        return False
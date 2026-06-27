class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window_size = len(s1)
        hash1 = {}
        hash2 = {}
        for i in s1:
            hash1[i] = hash1.get(i,0)+1
        p1=0
        p2=len(s1)
        while p2<=len(s2):
            for i in range(p1,p2):
                hash2[s2[i]] = hash2.get(s2[i],0)+1
            if hash1 == hash2:
                return True
            else:
                hash2 = {}
                p1+=1
                p2+=1
        return False
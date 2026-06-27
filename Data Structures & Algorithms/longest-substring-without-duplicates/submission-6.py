class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_sub = 0
        sub = 0
        p1=0
        p2=0
        contains = []
        while p2<len(s):
            if s[p2] in contains:
                max_sub = max(max_sub, len(contains))
                print(p1,p2,"before", max_sub)
                while s[p2] in contains:
                    contains.remove(s[p1])
                    p1+=1
                contains.append(s[p2])
                p2+=1
                print(p1,p2,"after", max_sub)
            else:
                contains.append(s[p2])
                p2+=1
        max_sub = max(max_sub, len(contains))
        return max_sub
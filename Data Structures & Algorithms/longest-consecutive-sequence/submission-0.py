class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res_hash = {}
        for i in nums:
            res_hash[i] = i+1

        max_count = 0
        for i in res_hash:
            if (i-1) not in res_hash:
                current = i
                count = 0
                while current in res_hash:
                    current = res_hash[current]
                    count += 1
                if count > max_count:
                    max_count = count
        return max_count
                                    
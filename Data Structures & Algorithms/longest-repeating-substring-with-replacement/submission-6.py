class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        p1 = 0
        p2 = 0
        max_count = 0
        frequency = {}

        while p2 < len(s):

            frequency[s[p2]] = frequency.get(s[p2], 0) + 1

            while len(frequency) > 1 and (p2-p1+1) - max(frequency.values()) > k:
                frequency[s[p1]] -= 1
                if frequency[s[p1]] == 0:
                    del frequency[s[p1]]
                p1 += 1

            count = p2 - p1 + 1
            max_count = max(max_count, count)

            p2 += 1

        return max_count

    def compare_frequency(self, frequency):
        vals = list(frequency.values())
        return [max(vals), min(vals)]
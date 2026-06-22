class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeated = {}
        result = []
        for i in nums:
            repeated[i] = repeated.get(i, 0) + 1
        
        sorted_items = sorted(repeated.items(), key=lambda x: x[1], reverse=True)

        count = 0
        for item in sorted_items:
            result.append(item[0])
            count += 1

            if count == k:
                break

        return result
        
            
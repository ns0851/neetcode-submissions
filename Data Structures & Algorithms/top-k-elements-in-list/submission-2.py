class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeated = {}
        result = []
        for i in nums:
            repeated[i] = repeated.get(i, 0) + 1
        
        sorted_dict = dict(sorted(repeated.items(), key=lambda x: x[1], reverse=True))
        print(sorted_dict)
        for i in sorted_dict:
            result.append(i)
        return result[:k]
        
            
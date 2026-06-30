from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ctr = dict(Counter(nums))
        sorted_occurences = [k for k, v in dict(sorted(ctr.items(), key=lambda item: item[1], reverse=True)).items()]
        return sorted_occurences[:k]
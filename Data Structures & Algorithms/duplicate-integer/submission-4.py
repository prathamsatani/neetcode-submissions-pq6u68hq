from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ctr = Counter(nums)
        for k, v in ctr.items():
            if v > 1:
                return True
        
        del ctr
        return False
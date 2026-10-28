from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ctr = Counter(s)

        for char in t:
            if char not in ctr:
                return False
            else:
                ctr[char] -= 1
        
        for v in ctr.values():
            if v > 0:
                return False
            
        return True
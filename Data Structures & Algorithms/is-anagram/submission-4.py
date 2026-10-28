from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        ctr1 = Counter(s)
        ctr2 = Counter(t)
        
        if dict(ctr1) == dict(ctr2):
            return True
        else:
            return False
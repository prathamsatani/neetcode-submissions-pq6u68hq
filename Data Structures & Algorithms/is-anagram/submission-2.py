from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ctr1 = dict(Counter(s))
        ctr2 = dict(Counter(t))

        return ctr1 == ctr2
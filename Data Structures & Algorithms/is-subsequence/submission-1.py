class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        if len(s) == 0:
            return True
        
        if len(t) == 0:
            return False
            
        for j in range(len(t)):
            if t[j] == s[i]:
                i += 1
                if i > len(s) - 1:
                    break
        
        if i == len(s):
            return True
        else:
            return False
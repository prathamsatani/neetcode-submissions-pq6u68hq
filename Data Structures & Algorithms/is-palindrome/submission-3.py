class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_d = ""
        for c in s:
            if c.isalnum():
                s_d += c.lower()

        i, j = 0, len(s_d) - 1
        while i <= j:
            if s_d[i] != s_d[j]:
                return False
            
            i += 1
            j -= 1
        
        return True

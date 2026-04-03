class Solution:
    def isPalindrome(self, s: str) -> bool:
        parsed = ""
        for char in s:
            if char.isalnum():
                parsed += char
        for i in range(int(len(parsed)/2)):
            if parsed[i].lower() != parsed[len(parsed) - i - 1].lower():
                return False
        
        return True
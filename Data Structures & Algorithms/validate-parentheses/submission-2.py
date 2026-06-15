class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False

        mapping = {
            "}": "{",
            "]": "[",
            ")": "("
        }
        stack = []
        for c in s:
            if c == "[" or c == "{" or c == "(":
                stack.append(c)
            elif c == "]" or c == "}" or c == ")":
                if len(stack) > 0 and mapping[c] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(c)
        
        if len(stack) == 0:
            return True
        else:
            return False

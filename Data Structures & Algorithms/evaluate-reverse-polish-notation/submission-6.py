class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y
        }
        
        for char in tokens:
            if char not in op:
                stack.append(int(char))
            else:
                v1 = stack.pop()
                v2 = stack.pop()
                res = op[char](int(v2), int(v1))
                stack.append(res)
        
        return int(stack.pop())
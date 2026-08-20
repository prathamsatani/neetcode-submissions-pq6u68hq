class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0 and len(self.minStack) == 0:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            if val <= self.minStack[-1]:
                self.minStack.append(val)
                self.stack.append(val)
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.minStack[-1]:
            self.stack.pop()
            self.minStack.pop()
        else:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

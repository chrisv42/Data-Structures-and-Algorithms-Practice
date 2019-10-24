class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.minStack) == 0 or x <= self.minStack[-1]:
            self.minStack.append(x)

    def pop(self) -> None:
        if len(self.stack) == 0:
            return None
        elif self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0: return None
        else: return self.stack[-1]

    def getMin(self) -> int:
        if len(self.minStack) == 0: return None
        else: return self.minStack[-1]

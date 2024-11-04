class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        item = [val, self.min]
        if self.min is None or val < self.min:
            self.min = val
        self.stack.append(item)

    def pop(self) -> None:
        item = self.stack.pop()
        if item[0] == self.min:
            self.min = item[1] # reset the current min which was item[1] before it was overwritten

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
        




minStack = MinStack()


minStack.push(0);
print(minStack.getMin())
minStack.push(1);
print(minStack.getMin())
minStack.push(0);
print(minStack.getMin())
print(minStack.pop())
print(minStack.getMin())


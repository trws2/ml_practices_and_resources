# runtime: O(n)
# space: O(n)

class MinStack:
    # one stack solution
    # each element in the stack has two numbers:
    # the regular number maintained by the stack and the 
    # current minimum number in the stack

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.stack.append((val, val))
            return
        min_val = self.stack[-1][1]
        min_val = min(min_val, val)
        self.stack.append((val, min_val))
        
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

    # # two stack solution
    # def __init__(self):
    #     self.stack = []
    #     self.min_stack = []

    # def push(self, val: int) -> None:
    #     self.stack.append(val)
    #     if len(self.min_stack) == 0:
    #         self.min_stack.append(val)
    #         return
    #     # it is important to use >=, as there can 
    #     # be duplicate minimum element put to the stack
    #     if self.min_stack[-1] >= val:
    #         self.min_stack.append(val)

    # def pop(self) -> None:
    #     val = self.stack.pop()
    #     if val == self.min_stack[-1]:
    #         self.min_stack.pop()

    # def top(self) -> int:
    #     return self.stack[-1]        

    # def getMin(self) -> int:
    #     return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


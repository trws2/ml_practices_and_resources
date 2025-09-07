# stack s1 is only for push and stack s2 is only for pop/peek
# front and s2 can be used together to make peek run faster
# reference editorial solution in https://leetcode.com/problems/implement-queue-using-stacks/solutions/127533/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.front = None
        self.s1 = []
        self.s2 = []

    # runtime O(1)
    # space O(n)
    def push(self, x: int) -> None:
        if len(self.s1) == 0:
            self.front = x
        self.s1.append(x)

    # runtime amortized O(1)
    # space O(1)
    # smart
    def pop(self) -> int:
        if len(self.s2) == 0:
            while (len(self.s1) > 0):
                self.s2.append(self.s1.pop())
        return self.s2.pop()
    
    # runtime O(1)
    # space O(1)a
    # smart
    def peek(self) -> int:
        if (len(self.s2) > 0):
            return self.s2[-1]
        return self.front

    # runtime O(1)
    # space O(1)
    def empty(self) -> bool:
        return len(self.s1) == 0 and len(self.s2) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

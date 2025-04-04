# runtime: O(n)
# space: O(n)

from collections import deque

class Solution:
    def calculate(self, s: str) -> int:

        def calculateAux(sub_queue: deque) -> int:
            left = None
            right = None
            op = None

            if sub_queue[0] == '-':
                sub_queue[1] = -sub_queue[1]
                sub_queue.popleft()
            for c in sub_queue:
                if c in ('+', '-'):
                    op = c
                elif left is None:
                    left = c
                elif right is None:
                    right = c

                if left is not None and right is not None and op is not None:
                    if op == '+':
                        left = left + right
                    else:
                        left = left - right
                    right = None
                    op = None

            return left

        queue = deque()

        num = []
        for c in s:
            if not c:
                continue
            if c in ('+', '(', ')'):
                if num:
                    if ''.join(num) == '-':
                        queue.append('-')
                    else:
                        queue.append(int(''.join(num)))
                    num = []
                queue.append(c)
            if c in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
                num.append(c)
            if c == '-':
                if not num and (len(queue) == 0 or queue[-1] == '('):
                    num.append(c) # negative sign, not minus operand
                else:
                    if num:
                        queue.append(int(''.join(num)))
                        num = []
                    queue.append(c)

        if num:
            queue.append(int(''.join(num)))
            num = []

        def finalCalculation() -> int:
            new_queue = deque()            
            if not queue:
                return new_queue
            while queue:
                c = queue.pop()
                if c == ')':
                    sub_queue = deque()
                    while queue:
                        c = queue.pop()
                        if c == '(':
                            res = calculateAux(sub_queue)
                            new_queue.appendleft(res)
                            break
                        elif c == ')':
                            res = finalCalculationPar() 
                            sub_queue.appendleft(res)
                        else:
                            sub_queue.appendleft(c)
                else:
                    new_queue.appendleft(c)
            return new_queue


        def finalCalculationPar() -> int:
            new_queue = deque()
            assert queue
            while queue:
                c = queue.pop()
                if c == '(':
                    res = calculateAux(new_queue)
                    return res
                elif c == ')':
                    res = finalCalculationPar()
                    new_queue.appendleft(res)
                else:
                    new_queue.appendleft(c)

        new_queue = finalCalculation()
        res = calculateAux(new_queue)

        return res

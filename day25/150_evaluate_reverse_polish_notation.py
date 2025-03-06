# runtime: O(n)
# space: O(n)

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                num = int(token)
                stack.append(num)
            except:
                left_operand = stack.pop()
                right_operand = stack.pop()                
                if token == '+':
                    res = right_operand + left_operand
                    stack.append(res)
                    continue
                if token == '-':
                    res = right_operand - left_operand
                    stack.append(res)
                    continue
                if token == '*':
                    res = right_operand * left_operand
                    stack.append(res)
                    continue                                        
                if token == '/':
                    res = int(right_operand / left_operand)
                    stack.append(res)
                    continue

        return stack[-1]

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
                right_op = stack.pop()
                left_op = stack.pop()                
                if token == '+':
                    new_num = left_op + right_op
                elif token == '-':
                    new_num = left_op - right_op
                elif token == '*':
                    new_num = left_op * right_op
                elif token == '/':
                    new_num = int(left_op / right_op)
                stack.append(new_num)
        
        return stack[-1]


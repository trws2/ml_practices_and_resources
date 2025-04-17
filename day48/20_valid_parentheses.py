# runtime: O(n)
# space: O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i, c in enumerate(s):
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == ')':
                if not stack or stack.pop() != ')':
                    return False
            elif c == ']':
                if not stack or stack.pop() != ']':
                    return False
            elif c == '}':
                if not stack or stack.pop() != '}':
                    return False

        return not stack                                  

# newer
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
                continue
            if c == '[':
                stack.append(']')
                continue
            if c == '{':
                stack.append('}')
                continue
            else:
                if len(stack) == 0:
                    return False
                latest = stack.pop()
                if latest != c:
                    return False

        return len(stack) == 0


# older
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

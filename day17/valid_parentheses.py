# runtime: O(n)
# space: O(n)
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
            else:
                if len(stack) == 0:
                    return False
                pre = stack.pop()
                if pre != c:
                    return False
            
        return len(stack) == 0

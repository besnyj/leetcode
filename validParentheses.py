class Solution:
    def isValid(self: str) -> bool:

        pairs = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        stack = []

        for char in self:
            if char in '([{':
                stack.append(char)
            elif char != pairs[stack.pop()] or len(self) == 0:
                return False
        return True
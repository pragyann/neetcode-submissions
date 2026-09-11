class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in bracket_pair:
                if not stack:
                    return False

                if stack.pop() != bracket_pair[c]:
                    return False
                
            else:
                stack.append(c)

        return len(stack) == 0
        
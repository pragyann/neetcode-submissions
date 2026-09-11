class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_pair = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in bracket_pair.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False

                opening = stack.pop()

                if opening != bracket_pair[c]:
                    return False

        return len(stack) == 0
        
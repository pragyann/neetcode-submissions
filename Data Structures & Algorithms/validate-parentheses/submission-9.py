class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paran_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c in paran_map:
                if stack and stack[-1] == paran_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

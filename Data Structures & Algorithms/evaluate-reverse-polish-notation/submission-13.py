class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        for t in tokens:
            if t in operators:
                o2, o1 = stack.pop(), stack.pop()
                res = self.operate(o1, o2, t)
                stack.append(res)
            else:
                stack.append(int(t))
        print(stack)
        return stack[0]

    def operate(self, o1, o2, op):
        if op == '+':
            return o1 + o2
        elif op == '-':
            return o1 - o2
        elif op == '*':
            return o1 * o2
        else:
            return int(o1 / o2)

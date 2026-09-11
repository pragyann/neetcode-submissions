class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()

        for token in tokens:
            print(stack)
            if self.isOp(token):
                if len(stack) < 2:
                    raise Exception("Invalid Input")
                
                op2, op1 = stack.pop(), stack.pop()

                res = self.performOp(op1, op2, token)
                stack.append(res)
            else:
                stack.append(int(token))
            print(stack)
            print('\n')
        return stack[0]


    def performOp(self, op1, op2, op):
        if op == "+": return op1 + op2
        if op == "-": return op1 - op2
        if op == "*": return op1 * op2
        if op == "/": return int(op1/op2)
    
    def isOp(self, val):
        return val in ['+', '-', '*', '/']
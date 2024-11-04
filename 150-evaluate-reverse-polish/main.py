class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        i = 0
        operands = "+-*/"
        while i < len(tokens):
            print(stack)
            if tokens[i] in operands:
                operand = tokens[i]
                b, a = stack.pop(), stack.pop()
                res = None
                if operand == "+":
                    res = a + b
                elif operand == "-":
                    res = a - b
                elif operand == "*":
                    res = a * b
                else:
                    res = math.trunc(0, a // b)
                stack.append(res)
            else:
                stack.append(int(tokens[i]))
            i+=1

        return stack[-1]



sol = Solution()
inp = ["2","1","+","3","*"]
inp = ["4","13","5","/","+"]
inp = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
inp = ["4","-2","/","2","-3","-","-"]
print(sol.evalRPN(inp))

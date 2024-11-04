from typing import Tuple
class Solution:
    def calculate(self, s: str) -> int:

        return self.process(s, 0)


    def process(self, s: str, i: int) -> int:
        res = 0
        sign = 1
        stack = []
        num = 0
        while i < len(s):
            print(f"res {res} num {num}")
            if s[i].isdigit():
                print(f"digit {s[i]}")
                num = num * 10 + ord(s[i]) - ord('0')
                print(f"num {num}")
            elif s[i] in "+-":
                print(f"{res} + {num} * {sign}")
                res = res + sign * num
                sign = 1 if s[i] == '+' else -1
                num = 0
                print(f"num {num} res {res} sign {sign}")
            elif s[i] == '(':
                print("sub problem")
                stack.append(res)
                stack.append(sign)
                print(stack)
                res = 0
                sign = 1
            elif s[i] == ')':
                print("sub prob")
                sign_before, temp_res = stack.pop(), stack.pop() 
                print(temp_res, sign_before, res)
                res = temp_res + sign_before * res  + num 
                print(f"res {res}")
            elif s[i] == " ":
                pass
            else:
                print(f"{res} + {num} * {sign}")
                num = 0
                res = res + num * sign
            i += 1

        return res + num * sign 

sol = Solution()
# print(sol.calculate())
print(sol.calculate(" 2-1 + 2 "))

print(sol.calculate("1 + 1"))
print(sol.calculate(" 2-1 + 2 "))
print(sol.calculate("(1+(4+5+2)-3)+(6+8)"))
print(sol.calculate("1-(     -2)"))

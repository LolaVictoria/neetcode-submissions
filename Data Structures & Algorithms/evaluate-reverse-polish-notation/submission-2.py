class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops =['+', '-', '*', '/']

        for i in range(len(tokens)):
            if tokens[i] in ops:
                
                num_1 = stack.pop()
                num_2 = stack.pop()
                if tokens[i] == "+":
                    op_num = int(num_1) + int(num_2)
                elif tokens[i] == "-":
                    op_num = int(num_2) - int(num_1)
                elif tokens[i] == "*":
                    op_num = int(num_2) * int(num_1)
                else:
                    op_num = int(int(num_2) / int(num_1))
                stack.append(str(op_num))
            else:
                stack.append(tokens[i])
        return int(stack[-1])


        
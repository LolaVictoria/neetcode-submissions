class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hash_stack = {
            "]": "[",
            "}" : "{",
            ")" : "("
        }

        for i in s:
            if i in hash_stack:
                if stack and hash_stack[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i) 
        return len(stack) == 0
        
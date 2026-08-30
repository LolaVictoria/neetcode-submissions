class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(open_count, close_count, comb):
            if open_count == close_count == n:
                res.append(comb)
            
            if open_count < n:
                backtrack(open_count + 1, close_count, comb + '(')
            if close_count < open_count:
                backtrack(open_count, close_count + 1, comb + ')')
            
        backtrack(0, 0, "")
        return res
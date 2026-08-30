class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        letters = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        def backtrack(idx, comb):
            if idx == len(digits):
                res.append(comb)
                return
            
            for char in letters[int(digits[idx])]:
                backtrack(idx + 1, comb + char)
            
            
        backtrack(0, "")
        return res
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(idx, combo):
            if idx == len(s):
                res.append(combo[:])
            
            for i in range(idx, len(s)):
                piece = s[idx: i + 1]
                if piece == piece[::-1]:
                    combo.append(piece)
                    backtrack(i + 1, combo)
                    combo.pop()
        backtrack(0, [])
        return res

        
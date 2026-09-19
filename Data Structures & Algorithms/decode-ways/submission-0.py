class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def backtrack(idx):
            if idx == len(s):
                return 1
            if s[idx] == '0':
                return 0
            if idx in memo:
                return memo[idx]
            ways = backtrack(idx + 1)

            if idx + 1 < len(s) and int(s[idx:idx + 2]) <= 26:
                ways += backtrack(idx + 2)
            memo[idx] = ways
            return ways
        return backtrack(0)
        
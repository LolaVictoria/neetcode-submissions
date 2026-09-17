class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_substr = ""

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]


        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            if len(odd) > len(max_substr):
                max_substr = odd
            if len(even) > len(max_substr):
                max_substr = even
        return max_substr
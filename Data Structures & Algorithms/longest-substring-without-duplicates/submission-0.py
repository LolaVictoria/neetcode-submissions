class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow = 0
        seen = set()
        max_length = 0

        for fast in range(len(s)):
            while s[fast] in seen:
                seen.remove(s[slow])
                slow += 1

            seen.add(s[fast])
            max_length = max(max_length, fast - slow + 1) 
        return max_length



        
        
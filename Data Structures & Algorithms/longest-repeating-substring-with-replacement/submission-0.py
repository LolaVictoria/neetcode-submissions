class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = {}
        max_frequency = 0
        slow = 0
        max_length = 0
        
        for fast in range(len(s)):
            if s[fast] not in count:
                count[s[fast]] = 0
            count[s[fast]] += 1

            max_frequency = max(max_frequency, count[s[fast]])

            window_length = fast - slow + 1
            replacements = window_length - max_frequency

            if replacements > k:
                count[s[slow]] -= 1
                slow += 1

            window_length = fast - slow + 1
            max_length = max(max_length, window_length)
        return max_length
            
        
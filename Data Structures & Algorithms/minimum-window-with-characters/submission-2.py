class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}

        for i in t:          
            need[i] = need.get(i, 0) + 1
        
        res = ""
        min_length = float('inf')
        have = {}
        start = 0
        required = len(need)
        formed = 0
        for end in range(len(s)):
            char = s[end]
            if char in need:
                have[char] = have.get(char, 0) + 1
               
                if have[char] == need[char]:
                    formed += 1
            while formed == required:
                window_length = end - start + 1
                
                if window_length < min_length:
                    min_length = window_length
                    res = s[start:end + 1]

                left_char = s[start]

                if left_char in need:
                    have[left_char] -= 1

                    if have[left_char] < need[left_char]:
                        formed -= 1
                start += 1
            
        return res

            


        


        
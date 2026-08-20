class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sub_s1 = {}
        sub_s2 = {}
        start = 0

        for i in range(len(s1)):
            sub_s1[s1[i]] = sub_s1.get(s1[i], 0) + 1
            

        for end in range(len(s2)):
            sub_s2[s2[end]] = sub_s2.get(s2[end], 0) + 1
            
            if end - start + 1 > len(s1):
                sub_s2[s2[start]] -= 1

                if sub_s2[s2[start]] == 0:
                    del sub_s2[s2[start]]

                start += 1
            if sub_s2 ==  sub_s1:
                return True
        return False
           
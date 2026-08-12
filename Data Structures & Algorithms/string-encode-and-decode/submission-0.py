class Solution:
    

    def encode(self, strs: List[str]) -> str:
        enc = ""
        for word in strs:
            enc += str(len(word)) + "#" + word
        return enc
        


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            count = int(s[i:j])
            word = ""
            char = j + 1
            while count > 0:
                word += s[char]
                char += 1
                count -= 1
            res.append(word)
            i = char
        return res











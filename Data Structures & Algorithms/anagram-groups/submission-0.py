class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        res = []
        for i in range(len(strs)):
            sort_word = tuple(sorted(strs[i]))
            if sort_word not in hash_map:
                hash_map[sort_word] = []
            hash_map[sort_word].append(strs[i])

        for i in hash_map.values():
            res.append(i)
        return res
            
        
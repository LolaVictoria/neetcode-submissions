class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        res = []

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1
        
        while k > 0:
            max_key = max(hash_map, key=hash_map.get)
            res.append(max_key)
            del hash_map[max_key]
            k -= 1
        return res

        
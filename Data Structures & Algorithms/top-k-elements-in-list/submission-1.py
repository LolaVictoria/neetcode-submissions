class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for i in nums:
            hash_map[i] = hash_map.get(i, 0) + 1

        heap = [(-freq, num) for num, freq in hash_map.items()]
        heapq.heapify(heap)

        res = []

        while k > 0:
            freq, num = heapq.heappop(heap)
            res.append(num)
            k -= 1
        return res
        # hash_map = {}
        # res = []

        # for i in nums:
        #     hash_map[i] = hash_map.get(i, 0) + 1
        
        # while k > 0:
        #     max_key = max(hash_map, key=hash_map.get)
        #     res.append(max_key)
        #     del hash_map[max_key]
        #     k -= 1
        # return res

        
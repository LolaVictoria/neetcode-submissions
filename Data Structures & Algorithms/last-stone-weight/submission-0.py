class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in range(len(stones)):
            heapq.heappush(heap, -stones[i])
        
        while len(heap) > 1:
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)

            if first == second:
                continue
            elif first > second:
                curr = first - second
                heapq.heappush(heap, -curr)
        if len(heap) == 1:
            return -heapq.heappop(heap)
        return 0



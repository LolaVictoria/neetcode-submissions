class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(heap, (dist, x, y))
        res = []

        while k > 0:
            curr = heapq.heappop(heap)
            res.append([curr[1], curr[2]])
            k -= 1
        return res
            
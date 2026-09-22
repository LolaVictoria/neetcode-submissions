class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        
        for i in range(len(intervals)):
            if res and res[-1][1] >= intervals[i][0]:
                end = max(res[-1][1], intervals[i][1])
                res[-1] = [res[-1][0], end]
            else:
                res.append(intervals[i])
        return res



        
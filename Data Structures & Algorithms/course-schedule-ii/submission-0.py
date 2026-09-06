class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        visited = set()
        visiting = set()
        prereq = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        
        def dfs(curr):
            if curr in visited:
                return True
            if curr in visiting:
                return False  
            
            visiting.add(curr)
            for i in prereq[curr]:
                if not dfs(i):
                    return False
            visiting.remove(curr)
            visited.add(curr)
            res.append(curr)         
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return res
            
        
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereq[course].append(pre)
        visited = set()

        def dfs(curr):
            if curr in visited:
                return False
            if prereq[curr] == []:
                return True

            visited.add(curr)
            for i in prereq[curr]:
                if not dfs(i):
                    return False
            visited.remove(curr)
            prereq[curr] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

